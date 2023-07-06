from sqlalchemy import Column, String, Text

from app.core.config import CHARITY_NAME_MAX_LENGTH
from app.core.db import PreBaseDonationCharity


class CharityProject(PreBaseDonationCharity):
    name = Column(
        String(CHARITY_NAME_MAX_LENGTH), unique=True, nullable=False)
    description = Column(Text, nullable=False)

    def __repr__(self) -> str:
        return f'Фонд {self.name}'