"""
Finance Models
"""
from django.db import models
from auditlog.registry import auditlog
from core.models import BaseModel
from finance.choices import (
    COA_TYPE
)


class ChartOfAccounts(BaseModel):
    """
    Accounts defined per the business. Often abbreviated as COA
    """
    coa_type = models.PositiveSmallIntegerField(choices=COA_TYPE)
    account_code = models.CharField(max_length=30, unique=True)
    title = models.CharField(max_length=50, verbose_name="Account Name")
    description = models.CharField(max_length=200, verbose_name="Account Description")
    parent_account = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        ordering = ('coa_type', 'account_code')

    def __str__(self):
        return f'{self.account_code} - {self.title}'

    @staticmethod
    def is_credit_or_debit(coa, to_increase, coa_id=None):
        """
        Determine if the passed Chart of Account requires a debit or Credit

        Args:
            coa (ChartOfAccounts): Chart of Account object
            to_increase (bool): Do you want the Account to Increase or Decrease?
            coa_id (int): Chart of Account ID which is optional. If provided we use it to fetch the Chart of Account
        Returns:
             boo (bool): True if Credit, False if Debit. Else None

        #######################
        How To Use and Apply The Debit and Credit Rules:
        #######################

        (1) Determine the types of accounts the transactions affect-asset, liability, revenue, expense or draw account.
        (2) Determine if the transaction increases or decreases the account's balance.
        (3) Apply the debit and credit rules based on the type of account and whether the balance of the account will
        increase or decrease.

        Our Simple Debit / Credit Rule:

        All Accounts that Normally Have a Debit Balance are Increased with a Debit by placing the amount in the Left
        Column of the account and Decreased with a Credit by placing the amount in the Right Column of the account.
            ->Assets
            ->Draws
            ->Expenses
        All Accounts that Normally have a Credit Balance are Increased with a Credit by placing the amount in the Right
        Column of the account and Decreased with a Debit by placing the amount in the Left Column of the account.
            ->Liabilities
            ->Owner's Equity ( Capital )
            ->Revenue

        source: http://www.dwmbeancounter.com/tutorial/DrCrTChart.html

        """
        try:
            if not coa:
                if coa_id:
                    coa = ChartOfAccounts.objects.get(id=coa_id)
        except ChartOfAccounts.DoesNotExist:
            return None

        if coa.coa_type in [COA_TYPE.Asset, COA_TYPE.Expense]:
            if to_increase:
                return False
            else:
                return True
        elif coa.coa_type in [COA_TYPE.Liability, COA_TYPE.Equity, COA_TYPE.Income]:
            if to_increase:
                return True
            else:
                return False


auditlog.register(ChartOfAccounts)
