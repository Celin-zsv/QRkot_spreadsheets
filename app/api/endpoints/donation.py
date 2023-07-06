from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.core.user import current_superuser, current_user
from app.crud import charity_project_crud, donation_crud
from app.models import User
from app.schemas.donation import DonationAdminDB, DonationCreate, DonationDB
from app.services.investment import investment_process

router = APIRouter()


@router.get(
    '/',
    response_model=List[DonationAdminDB],
    response_model_exclude_none=True,
    dependencies=[Depends(current_superuser)]
)
async def get_all_donations(
        session: AsyncSession = Depends(get_async_session),
):
    """Получить все пожертвования. Доступ: суперпользователь."""
    return await donation_crud.get_multi(session=session)


@router.get(
    '/my',
    response_model=List[DonationDB],
    response_model_exclude_none=True
)
async def get_my_obj(
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_user)
):
    """
    Получить все пожертвования текущего пользователя.
    Доступ: авторизованный пользователь.
    """
    return await donation_crud.get_my_obj(
        session=session, user=user)


@router.post(
    '/',
    response_model=DonationDB,
    response_model_exclude_none=True
)
async def create_donation(
        donation_in: DonationCreate,
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_user)
):
    """Создать пожертвование. Доступ: авторизованный пользователь."""
    donation_db = await donation_crud.create(
        obj_in=donation_in, session=session, user=user)
    charity_projects_db = await charity_project_crud.get_open_objects(session)
    if charity_projects_db:
        investment_process(
            target=donation_db,
            sources=charity_projects_db
        )
    await session.commit()
    await session.refresh(donation_db)
    return donation_db
