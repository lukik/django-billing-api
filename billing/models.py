"""
Allow for the definition of simple billing structure
"""
from django.db import models
from auditlog.registry import auditlog
from core.models import BaseModel
from core.api_exceptions import MaxLoopException
from core.randomizer import generate_random, RANDOM
from partners.models import Partner
from billing.choices import INVOICE_STATUS


# ToDo: make this a variable in the DB in a settings table
LENGTH_INVOICE_NUMBER = 4

def generate_invoice_number(loop_counter=0):
    max_loop = 10
    try:
        while True:
            loop_counter += 1
            if loop_counter >= max_loop:
                # If function loops more than x times, raise an error
                raise MaxLoopException()
            code = generate_random(RANDOM.InvoiceNumber, LENGTH_INVOICE_NUMBER)
            try:
                Invoice.objects.get(invoice_number=code)
            except Invoice.DoesNotExist:
                return code
            continue
    except MaxLoopException:
        MaxLoopException()


class FeeItem(BaseModel):
    """
    Items that the business can charge for. i.e. Consulting, Counselling, Conveyancing
    """
    title = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=100, blank=True)
    coa = models.ForeignKey('finance.ChartOfAccounts', on_delete=models.CASCADE, null=True)
    display_sequence = models.SmallIntegerField(default=1)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['is_active', 'display_sequence']

    def __str__(self):
        return f'{self.title} - {self.description}'


class FeeStructure(BaseModel):
    """
    Fee structure for the business
    """
    fee_item = models.ForeignKey(FeeItem, on_delete=models.PROTECT, related_name='fee_structure')
    amount = models.DecimalField(max_digits=20, decimal_places=2, null=True)

    def __str__(self):
        return f'{self.fee_item.title} - {self.amount}'


class Invoice(BaseModel):
    """
    Simplified Invoice model to capture invoices raised by the Business.

    ToDo: Capture Invoice Line Items in a separate table
    """
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE)
    invoice_number = models.IntegerField(unique=True, default=generate_invoice_number)
    invoice_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField(null=True)
    terms = models.CharField(max_length=250, blank=True)
    status = models.PositiveSmallIntegerField(choices=INVOICE_STATUS)
    status_date = models.DateTimeField(auto_now=True)
    status_by = models.UUIDField(null=True, help_text='Related User')
    amount = models.DecimalField(max_digits=20, decimal_places=2)

    class Meta:
        ordering = ('-created_on',)

    def __str__(self):
        return f'{self.invoice_number} - {str(INVOICE_STATUS[self.status])}'


# Add models to Audit Log
auditlog.register(FeeItem)
auditlog.register(FeeStructure)
auditlog.register(Invoice)