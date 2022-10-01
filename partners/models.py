import os
from django.db import models
from auditlog.registry import auditlog
from server.settings import env
from core.models import BaseModel
from core.api_exceptions import MaxLoopException
from core.randomizer import generate_random, RANDOM
from partners.choices import PARTNER_STATUS

LENGTH_PARTNER_CODE = 6


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

    @staticmethod
    def create_new(created_by_id, title, notes, is_client, is_supplier, bulk_create=False):

        if not bulk_create:
            return Partner.objects.create(
                created_by_id=created_by_id, title=title, notes=notes,
                is_client=is_client, is_supplier=is_supplier
            )
        else:
            return Partner(
                created_by_id=created_by_id, title=title, notes=notes,
                is_client=is_client, is_supplier=is_supplier
            )


class PartnerUpload(BaseModel):
    """
    File uploaded by the business to upload partners in bulk
    """
    document = models.FileField(upload_to=env('PATH_PARTNER_IMPORT_FILE'))
    file_name = models.TextField(help_text='Name of File')
    upload_date = models.DateTimeField(auto_now_add=True)
    imported_successfully = models.BooleanField(null=True)
    import_summary = models.TextField(help_text="Summary of import")

    def __str__(self):
        return f'{self.file_name}'

    class Meta:
        ordering = ('-upload_date',)

# Add models to Audit Log
auditlog.register(Partner)

