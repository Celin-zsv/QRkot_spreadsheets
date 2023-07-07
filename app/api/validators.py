from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.charity_project import charity_project_crud
from app.models.charity_project import CharityProject
from app.schemas.charity_project import CharityProjectUpdate


async def check_name_obj_unique(
        obj_name: str,
        session: AsyncSession,
) -> None:
    """Проверить уникальность: наименование объекта."""
    charity_project = await charity_project_crud.get_obj_by_name(
        obj_name=obj_name,
        session=session)
    if charity_project is not None:
        raise HTTPException(
            status_code=400,
            detail='Проект с таким именем уже существует!')


async def check_obj_exists_by_id(
        obj_id: int,
        session: AsyncSession,
) -> CharityProject:
    """Проверить наличие объекта-БД по id."""
    charity_project_db = await charity_project_crud.get(
        obj_id=obj_id,
        session=session)
    if charity_project_db is None:
        raise HTTPException(
            status_code=404,
            detail='Проекта с указанным id не существует!')
    return charity_project_db


async def check_charity_project_before_edit(
        project_id: int,
        charity_project_in: CharityProjectUpdate,
        session: AsyncSession
) -> CharityProject:
    """Проверить проект: перед редактированием."""
    charity_project_db = await check_obj_exists_by_id(
        obj_id=project_id,
        session=session)
    if charity_project_db.close_date is not None:
        raise HTTPException(
            status_code=400,
            detail='Закрытый проект нельзя редактировать!')
    if (charity_project_in.full_amount and
            charity_project_db.invested_amount > charity_project_in.full_amount):
        raise HTTPException(
            status_code=400,
            detail='Нельзя установить требуемую сумму меньше уже вложенной')
    await check_name_obj_unique(
        obj_name=charity_project_in.name,
        session=session)
    return charity_project_db


async def check_charity_project_before_delete(
        project_id: int,
        session: AsyncSession
) -> CharityProject:
    """Проверить проект: перед удалением."""
    charity_project_db = await check_obj_exists_by_id(
        obj_id=project_id,
        session=session)
    if charity_project_db.invested_amount > 0:
        raise HTTPException(
            status_code=400,
            detail='В проект были внесены средства, не подлежит удалению!')
    if charity_project_db.fully_invested:
        raise HTTPException(
            status_code=400,
            detail='Закрытый проект нельзя редактировать!')
    return charity_project_db


def check_google_table_range(
    fact_column_count: int,
    constant_column_count: int,
    fact_row_count: int,
    constant_row_count: int
):
    if (
        fact_column_count > constant_column_count or
        fact_row_count > constant_row_count
    ):
        raise HTTPException(
            status_code=400,
            detail=f'Фактическое кол-во полей {fact_column_count} '
            f'допустимое - {constant_column_count}. '
            f'Фактическое кол-во строк {fact_row_count}, '
            f'допустимое - {constant_row_count}.')
