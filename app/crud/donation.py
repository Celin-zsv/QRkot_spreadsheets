from app.crud.base import CRUDBase
from app.models import Donation


class CRUDDonation(CRUDBase):
    pass


donation_crud = CRUDDonation(Donation)
