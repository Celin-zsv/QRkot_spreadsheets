from datetime import datetime

from aiogoogle import Aiogoogle

from app.core.config import (DRIVE_VERSION, FORMAT, MAJOR_DIMENSION,
                             PERMISSION_BODY_ROLE, PERMISSION_BODY_TYPE,
                             SHEET_COLUMN_COUNT, SHEET_HEADER_A1,
                             SHEET_HEADER_A2, SHEET_HEADER_A3, SHEET_HEADER_B3,
                             SHEET_HEADER_C3, SHEET_ID, SHEET_RANGE,
                             SHEET_ROW_COUNT, SHEET_TITLE, SHEET_TYPE,
                             SHEETS_VERSION, SPREADSHEET_LOCALE,
                             SPREADSHEET_TITLE, VALUE_INPUT_OPTION, settings)


async def spreadsheets_create(wrapper_services: Aiogoogle) -> str:
    service = await wrapper_services.discover('sheets', SHEETS_VERSION)
    spreadsheet_body = {
        'properties': {
            'title': SPREADSHEET_TITLE.format(datetime.now().strftime(FORMAT)),
            'locale': SPREADSHEET_LOCALE},
        'sheets': [
            {'properties': {'sheetType': SHEET_TYPE,
                            'sheetId': SHEET_ID,
                            'title': SHEET_TITLE,
                            'gridProperties': {
                                'rowCount': SHEET_ROW_COUNT,
                                'columnCount': SHEET_COLUMN_COUNT}}}]
    }
    response = await wrapper_services.as_service_account(
        service.spreadsheets.create(json=spreadsheet_body))
    return response['spreadsheetId']


async def set_user_permissions(
        spreadsheetid: str,
        wrapper_services: Aiogoogle
) -> None:
    permissions_body = {'type': PERMISSION_BODY_TYPE,
                        'role': PERMISSION_BODY_ROLE,
                        'emailAddress': settings.email}
    service = await wrapper_services.discover('drive', DRIVE_VERSION)
    await wrapper_services.as_service_account(
        service.permissions.create(
            fileId=spreadsheetid,
            json=permissions_body,
            fields='id'))


async def spreadsheets_update_value(
        spreadsheetid: str,
        charity_projects: list,
        wrapper_services: Aiogoogle
) -> None:
    service = await wrapper_services.discover('sheets', SHEETS_VERSION)
    table_values = [
        [SHEET_HEADER_A1, datetime.now().strftime(FORMAT)],
        [SHEET_HEADER_A2],
        [SHEET_HEADER_A3, SHEET_HEADER_B3, SHEET_HEADER_C3]
    ]
    for project in charity_projects:
        new_row = [
            str(project.name),
            str(project.close_date - project.create_date),
            str(project.description)
        ]
        table_values.append(new_row)

    update_body = {
        'majorDimension': MAJOR_DIMENSION,
        'values': table_values
    }
    await wrapper_services.as_service_account(
        service.spreadsheets.values.update(
            spreadsheetId=spreadsheetid,
            range=SHEET_RANGE.format(len(table_values)),
            valueInputOption=VALUE_INPUT_OPTION,
            json=update_body))
