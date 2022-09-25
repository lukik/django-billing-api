from django.db import models
from auditlog.registry import auditlog
from core.models import BaseModel
from core.api_exceptions import MaxLoopException
from core.randomizer import generate_random, RANDOM
from partners.choices import PARTNER_STATUS

LENGTH_PARTNER_CODE = 5


def generate_account_number(loop_counter=0):
    max_loop = 10
    try:
        while True:
            loop_counter += 1
            if loop_counter >= max_loop:
                # If function loops more than x times, raise an error
                raise MaxLoopException()
            code = generate_random(RANDOM.PartnerAccountNumber, LENGTH_PARTNER_CODE)
            try:
                Partner.objects.get(account_number=code)
            except Partner.DoesNotExist:
                return code
            continue
    except MaxLoopException:
        MaxLoopException()


class Partner(BaseModel):
    """
    Account that identifies the entities we do business with e.g. Clients, Suppliers etc
    """
    title = models.CharField(max_length=100, unique=True, help_text='Name to identify the partner account')
    account_number = models.CharField(max_length=LENGTH_PARTNER_CODE, unique=True,
                                      default=generate_account_number,
                                      help_text='Number to identify the partner account')
    status = models.PositiveSmallIntegerField(choices=PARTNER_STATUS, default=PARTNER_STATUS.Active)
    notes = models.CharField(max_length=250, blank=True, default="", help_text='Supporting text')
    is_client = models.BooleanField()
    is_supplier = models.BooleanField()

    def __str__(self):
        return f'{self.title} - {self.account_number}'


# Add models to Audit Log
auditlog.register(Partner)

