from django.db import models
from auditlog.registry import auditlog
from core.models import BaseModel
from partners.choices import PARTNER_STATUS


class Partner(BaseModel):
    """
    Account that identifies the entities we do business with e.g. Clients, Suppliers etc
    """
    title = models.TextField(unique=True, help_text='Name to identify the partner account')
    account_number = models.TextField(unique=True, help_text='Number to identify the partner account')
    status = models.PositiveSmallIntegerField(choices=PARTNER_STATUS, default=PARTNER_STATUS.Active)
    notes = models.CharField(max_length=250, blank=True, default="", help_text='Supporting text')
    is_client = models.BooleanField()
    is_supplier = models.BooleanField()


# Add models to Audit Log
auditlog.register(Partner)

