from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Extra, Field, PositiveInt

from app.core.config import (CHARITY_NAME_MAX_LENGTH, CHARITY_NAME_MIN_LENGTH,
                             DESCRIPTION_NAME_MIN_LENGTH)


class CharityProjectBase(BaseModel):
    """Charity. Базовый класс."""
    name: Optional[str] = Field(
        None,
        min_length=CHARITY_NAME_MIN_LENGTH,
        max_length=CHARITY_NAME_MAX_LENGTH)
    description: Optional[str] = Field(
        None,
        min_length=DESCRIPTION_NAME_MIN_LENGTH)
    full_amount: Optional[PositiveInt]

    class Config:
        extra = Extra.forbid


class CharityProjectCreate(CharityProjectBase):
    """Charity. Создать объект БД. Доступ: суперпользователь."""
    name: str = Field(
        min_length=CHARITY_NAME_MIN_LENGTH,
        max_length=CHARITY_NAME_MAX_LENGTH)
    description: str = Field(
        min_length=DESCRIPTION_NAME_MIN_LENGTH)
    full_amount: PositiveInt


class CharityProjectUpdate(CharityProjectBase):
    """Charity. Редактировать объект БД. Доступ: суперпользователь."""
    pass


class CharityProjectDB(CharityProjectCreate):
    """Charity. Получить объект БД. Доступ: любой пользователь."""
    id: int
    invested_amount: int
    fully_invested: bool
    create_date: datetime
    close_date: Optional[datetime]

    class Config:
        orm_mode = True
