from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Extra, PositiveInt


class DonationBase(BaseModel):
    """Donation. Базовый класс."""
    full_amount: Optional[PositiveInt]
    comment: Optional[str]

    class Config:
        extra = Extra.forbid


class DonationCreate(DonationBase):
    """Donation. Создать объект БД. Доступ: авторизованный пользователь."""
    full_amount: PositiveInt


class DonationDB(DonationCreate):
    """Donation. Получить объект БД. Доступ: авторизованный пользователь."""
    id: int
    create_date: datetime

    class Config:
        orm_mode = True


class DonationAdminDB(DonationDB):
    """Donation. Получить объект БД. Доступ: суперюзер."""
    user_id: Optional[int]
    invested_amount: int
    fully_invested: bool
    close_date: Optional[datetime]
