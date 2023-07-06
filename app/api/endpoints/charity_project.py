from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.validators import (check_charity_project_before_delete,
                                check_charity_project_before_edit,
                                check_name_obj_unique)
from app.core.db import get_async_session
from app.core.user import current_superuser
from app.crud import charity_project_crud, donation_crud
from app.schemas.charity_project import (CharityProjectCreate,
                                         CharityProjectDB,
                                         CharityProjectUpdate)
from app.services.investment import investment_process

router = APIRouter()


@router.post(
    '/',
    response_model=CharityProjectDB,
    response_model_exclude_none=True,
    dependencies=[Depends(current_superuser)]
)
async def create_new_charity_project(
        charity_project_in: CharityProjectCreate,
        session: AsyncSession = Depends(get_async_session),
):
    """Создать проект. Доступ: суперпользователь."""
    await check_name_obj_unique(
        obj_name=charity_project_in.name,
        session=session)
    charity_project_db = await charity_project_crud.create(
        obj_in=charity_project_in,
        session=session)
    donations_db = await donation_crud.get_open_objects(session)
    if donations_db:
        investment_process(
            target=charity_project_db,
            sources=donations_db)
    await session.commit()
    await session.refresh(charity_project_db)
    return charity_project_db


@router.get(
    '/',
    response_model=List[CharityProjectDB],
    response_model_exclude_none=True,
)
async def get_all_charity_projects(
        session: AsyncSession = Depends(get_async_session),
):
    """Получить все проекты. Доступ: любой пользователь."""
    return await charity_project_crud.get_multi(session=session)


@router.patch(
    '/{project_id}',
    response_model=CharityProjectDB,
    dependencies=[Depends(current_superuser)]
)
async def update_charity_project(
        project_id: int,
        charity_project_in: CharityProjectUpdate,
        session: AsyncSession = Depends(get_async_session),
):
    """Редактировать проект. Доступ: суперпользователь."""
    charity_project_db = await check_charity_project_before_edit(
        project_id=project_id,
        charity_project_in=charity_project_in,
        session=session)
    charity_project_db = await charity_project_crud.update(
        db_obj=charity_project_db,
        obj_in=charity_project_in,
        session=session)
    return charity_project_db


@router.delete(
    '/{project_id}',
    response_model=CharityProjectDB,
    dependencies=[Depends(current_superuser)]
)
async def remove_charity_project(
        project_id: int,
        session: AsyncSession = Depends(get_async_session),
):
    """Удалить проект. Доступ: суперпользователь."""
    charity_project_db = await check_charity_project_before_delete(
        project_id=project_id,
        session=session)
    charity_project_db = await charity_project_crud.delete(
        db_obj=charity_project_db,
        session=session)
    return charity_project_db
