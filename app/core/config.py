from typing import Optional

from pydantic import BaseSettings, EmailStr

CHARITY_NAME_MAX_LENGTH = 100
CHARITY_NAME_MIN_LENGTH = 1
DESCRIPTION_NAME_MIN_LENGTH = 1

FORMAT = "%Y/%m/%d %H:%M:%S"
SPREADSHEET_TITLE = 'Отчет от {}'
SPREADSHEET_LOCALE = 'ru_RU'
SHEET_TYPE = 'GRID'
SHEET_ID = 0
SHEET_TITLE = 'Закрытые проекты'
SHEET_ROW_COUNT = 100
SHEET_COLUMN_COUNT = 3
SHEET_RANGE = 'A1:C{}'
SHEET_HEADER_A1 = 'Отчет от'
SHEET_HEADER_A2 = 'Топ проектов по скорости закрытия'
SHEET_HEADER_A3 = 'Название проекта'
SHEET_HEADER_B3 = 'Время сбора'
SHEET_HEADER_C3 = 'Описание'
SHEETS_VERSION = 'v4'
DRIVE_VERSION = 'v3'
PERMISSION_BODY_TYPE = 'user'
PERMISSION_BODY_ROLE = 'writer'
MAJOR_DIMENSION = 'ROWS'
VALUE_INPUT_OPTION = 'USER_ENTERED'


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
