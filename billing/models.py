"""
Allow for the definition of simple billing structure
"""
from django.db import models
from auditlog.registry import auditlog
from core.models import BaseModel


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


# Add models to Audit Log
auditlog.register(FeeItem)
auditlog.register(FeeStructure)
