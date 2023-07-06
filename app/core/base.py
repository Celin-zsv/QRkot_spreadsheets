"""Импорт класса Base и всех моделей для Alembic."""
from app.core.db import Base, PreBaseDonationCharity  # noqa
from app.models import CharityProject, Donation, User  # noqa