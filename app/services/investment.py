from datetime import datetime
from typing import List, Union

from app.models import CharityProject, Donation


def close_obj(obj: Union[CharityProject, Donation]) -> None:
    obj.fully_invested = True
    obj.close_date = datetime.now()


def investment_process(
    target: Union[CharityProject, Donation],
    sources: List[Union[CharityProject, Donation]]
) -> None:
    free_target_amount = target.full_amount
    for source in sources:
        free_amount = min(
            free_target_amount, source.full_amount - source.invested_amount)
        source.invested_amount += free_amount
        target.invested_amount += free_amount
        free_target_amount -= free_amount
        if source.full_amount == source.invested_amount:
            close_obj(source)
        if not free_target_amount:
            close_obj(target)
            break
