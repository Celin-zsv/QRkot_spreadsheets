from typing import Optional

from pydantic import BaseSettings, EmailStr

CHARITY_NAME_MAX_LENGTH = 100
CHARITY_NAME_MIN_LENGTH = 1
DESCRIPTION_NAME_MIN_LENGTH = 1

FORMAT = "%Y/%m/%d %H:%M:%S"
SHEET_ROW_COUNT = 100
SHEET_COLUMN_COUNT = 3
SHEET_RANGE = 'A1:C{}'
PERMISSION_BODY_TYPE = 'user'
PERMISSION_BODY_ROLE = 'writer'
MAJOR_DIMENSION = 'ROWS'
VALUE_INPUT_OPTION = 'USER_ENTERED'
SPREADSHEET_BODY = dict(
    properties=dict(
        title='Отчет от {}',
        locale='ru_RU'
    ),
    sheets=[
        dict(
            properties=dict(
                sheetType='GRID',
                sheetId=0,
                title='Закрытые проекты',
                gridProperties=dict(
                    rowCount=SHEET_ROW_COUNT,
                    columnCount=SHEET_COLUMN_COUNT
                )
            )
        )
    ]
)
TABLE_VALUES = [
    ['Отчет от '],
    ['Топ проектов по скорости закрытия'],
    ['Название проекта', 'Время сбора', 'Описание']
]


class Settings(BaseSettings):
    app_title: str = 'Титл: Сервис благотворительного фонда'
    description: str = 'Описание сервиса'
    database_url: str = 'sqlite+aiosqlite:///./fastapi.db'
    secret: str = 'SECRET'
    first_superuser_email: Optional[EmailStr] = None
    first_superuser_password: Optional[str] = None
    type: Optional[str] = None
    project_id: Optional[str] = None
    private_key_id: Optional[str] = None
    private_key: Optional[str] = None
    client_email: Optional[str] = None
    client_id: Optional[str] = None
    auth_uri: Optional[str] = None
    token_uri: Optional[str] = None
    auth_provider_x509_cert_url: Optional[str] = None
    client_x509_cert_url: Optional[str] = None
    email: Optional[str] = None

    class Config:
        env_file = '.env'


settings = Settings()
