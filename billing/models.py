"""
Allow for the definition of simple billing structure
"""
from django.db import models
from auditlog.registry import auditlog
from core.models import BaseModel
from partners.models import Partner
from billing.choices import INVOICE_STATUS, INVOICE_DETAIL_TYPE, LINE_ITEM_STATUS


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
    Invoice raised by the Business
    """
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE)
    invoice_number = models.IntegerField(unique=True)
    invoice_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField(null=True)
    terms = models.CharField(max_length=250, blank=True)
    status = models.PositiveSmallIntegerField(choices=INVOICE_STATUS)
    status_date = models.DateTimeField(auto_now=True)
    status_by = models.UUIDField(null=True, help_text='Related User')

    class Meta:
        ordering = ('-created_on',)

    def __str__(self):
        return f'{self.invoice_number} - {str(INVOICE_STATUS[self.status])}'


class InvoiceDetail(BaseModel):
    """
    Amounts related to an invoice.
    """
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name="invoice_details")
    detail_type = models.PositiveSmallIntegerField(choices=INVOICE_DETAIL_TYPE)
    line_item = models.ForeignKey("self", on_delete=models.CASCADE, null=True, related_name="line_items",
                                  help_text="The line item the entry is related to")
    line_item_status = models.PositiveSmallIntegerField(choices=LINE_ITEM_STATUS, null=True,
                                                        help_text="Applies to items of Detail Type LineItem")
    line_item_status_date = models.DateTimeField(null=True)
    fee_item = models.ForeignKey(FeeItem, on_delete=models.CASCADE, null=True, related_name="fee_items")
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    description = models.CharField(max_length=250, blank=True)
    trx_ref_number = models.TextField(blank=True, help_text='Code to identify the transaction')
    trx_time = models.DateTimeField()
    is_cancelled = models.BooleanField(default=False)
    reason_cancelled = models.CharField(max_length=100, blank=True)
    cancelled_by = models.UUIDField(null=True, editable=False, help_text='Related User')

    def __str__(self):
        return f'{self.invoice.invoice_number} - {self.description} - {self.amount}'


# Add models to Audit Log
auditlog.register(FeeItem)
auditlog.register(FeeStructure)
auditlog.register(Invoice)
auditlog.register(InvoiceDetail)