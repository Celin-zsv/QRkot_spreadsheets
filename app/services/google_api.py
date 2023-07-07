from copy import deepcopy
from datetime import datetime

from aiogoogle import Aiogoogle

from app.api.validators import check_google_table_range
from app.core.config import (FORMAT, MAJOR_DIMENSION, PERMISSION_BODY_ROLE,
                             PERMISSION_BODY_TYPE, SHEET_COLUMN_COUNT,
                             SHEET_RANGE, SHEET_ROW_COUNT, SPREADSHEET_BODY,
                             TABLE_VALUES, VALUE_INPUT_OPTION, settings)


def get_table_json(data=SPREADSHEET_BODY):
    data = deepcopy(data)
    data['properties']['title'] += datetime.now().strftime(FORMAT)
    return data


async def spreadsheets_create(wrapper_services: Aiogoogle) -> str:
    service = await wrapper_services.discover('sheets', 'v4')
    response = await wrapper_services.as_service_account(
        service.spreadsheets.create(json=get_table_json()))
    return response['spreadsheetId']


async def set_user_permissions(
        spreadsheetid: str,
        wrapper_services: Aiogoogle
) -> None:
    permissions_body = {'type': PERMISSION_BODY_TYPE,
                        'role': PERMISSION_BODY_ROLE,
                        'emailAddress': settings.email}
    service = await wrapper_services.discover('drive', 'v3')
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
    service = await wrapper_services.discover('sheets', 'v4')
    table_values = deepcopy(TABLE_VALUES)
    table_values[0].append(datetime.now().strftime(FORMAT))
    for project in charity_projects:
        new_row = [
            project.name,
            str(project.close_date - project.create_date),
            project.description
        ]
        table_values.append(new_row)

    check_google_table_range(
        max(map(len, table_values)), SHEET_COLUMN_COUNT,
        len(table_values), SHEET_ROW_COUNT)

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
