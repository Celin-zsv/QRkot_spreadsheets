from typing import Optional

from fastapi.encoders import jsonable_encoder
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import User


class CRUDBase:
    """CRUD. Базовый класс."""
    def __init__(self, model):
        self.model = model

    async def get(
            self,
            obj_id: int,
            session: AsyncSession,
    ):
        """Получить объект по id."""
        db_obj = await session.execute(
            select(self.model).where(
                self.model.id == obj_id))
        return db_obj.scalars().first()

    async def get_multi(
            self,
            session: AsyncSession
    ):
        """Получить все объекты."""
        db_objs = await session.execute(select(self.model))
        return db_objs.scalars().all()

    async def get_open_objects(
            self,
            session: AsyncSession
    ):
        """Получить открытые объекты. Сортировка по дате создания."""
        open_obj = await session.execute(
            select(self.model).where(
                self.model.fully_invested.is_(False)
            ).order_by(self.model.create_date))
        return open_obj.scalars().all()

    async def create(
            self,
            obj_in,
            session: AsyncSession,
            user: Optional[User] = None
    ):
        """Создать объект."""
        obj_in_data = obj_in.dict()
        if user is not None:
            obj_in_data['user_id'] = user.id
        db_obj = self.model(**obj_in_data)
        session.add(db_obj)
        await session.commit()
        await session.refresh(db_obj)
        return db_obj

    async def update(
            self,
            db_obj,
            obj_in,
            session: AsyncSession,
    ):
        """Редактировать объект."""
        obj_data = jsonable_encoder(db_obj)
        update_data = obj_in.dict(exclude_unset=True)
        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])
        session.add(db_obj)
        await session.commit()
        await session.refresh(db_obj)
        return db_obj

    async def delete(
            self,
            db_obj,
            session: AsyncSession,
    ):
        """Удалить объект."""
        await session.delete(db_obj)
        await session.commit()
        return db_obj

    async def get_obj_by_name(
            self,
            obj_name: str,
            session: AsyncSession,
    ):
        """Вернуть объект по наименованию."""
        db_obj = await session.execute(
            select(self.model).where(
                self.model.name == obj_name))
        return db_obj.scalars().first()

    async def get_my_obj(
            self,
            session: AsyncSession,
            user: User
    ):
        """Получить объекты current user. Доступ: авторизованный user."""
        donations = await session.execute(
            select(self.model).where(
                self.model.user_id == user.id))
        return donations.scalars().all()
