"""
Finance Models
"""
from django.db import models
from auditlog.registry import auditlog
from core.models import BaseModel
from partners.models import Partner
from finance.choices import (
    COA_TYPE, JOURNAL_ENTRY_STATUS, JOURNAL_ENTRY_TYPE
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


class GeneralJournal(BaseModel):
    """
    General Journal/Ledger Entries
    """
    coa = models.ForeignKey(ChartOfAccounts, on_delete=models.CASCADE)
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE, null=True,
                                help_text='Entity linked to the transaction')
    amount = models.DecimalField(max_digits=20, decimal_places=2, help_text='Amount transacted')
    trx_ref_number = models.CharField(max_length=50, blank=True, help_text='Transaction reference number')
    trx_date = models.DateTimeField(help_text='Date the customer made the transaction')
    is_credit = models.BooleanField(help_text='True = Is Credit, False = Debit')
    narration = models.CharField(max_length=200, help_text='Specific narration for each transaction')
    status = models.PositiveSmallIntegerField(choices=JOURNAL_ENTRY_STATUS, default=JOURNAL_ENTRY_STATUS.Posted,
                                              help_text='Entry status e.g. Valid, Posted etc')
    entry_type = models.PositiveSmallIntegerField(choices=JOURNAL_ENTRY_TYPE, default=JOURNAL_ENTRY_TYPE.SystemEntry,
                                                  help_text='Entry by person or by the system?')

    def __str__(self):
        return f'{self.coa} - {self.amount}'

    @staticmethod
    def create_new(user_id, coa_id, partner_id, is_credit, amount, trx_ref_number, trx_date,
                   narration, entry_type, bulk_create):
        """
        Args:
            user_id (UUID):
            coa_id (UUID): Chart of Account ID that is being affected
            partner_id (UUID): entity being impacted by the posting
            is_credit (bool): Whether it's a credit or debit entry. True is Credit, False is Debit
            amount (Decimal):
            trx_ref_number (str):
            trx_date (DateTime): Date the customer paid
            narration (str): Narration for the transaction
            entry_type (int): Determine if entry is Manual or Automated
            bulk_create (bool): True is a bulk entry, False is direct object creation
        Returns:
            GeneralJournal
        """
        if bulk_create:
            # Bulk Create
            return GeneralJournal(
                created_by_id=user_id, coa_id=coa_id, partner_id=partner_id,
                is_credit=is_credit, amount=amount,
                trx_ref_number=trx_ref_number, trx_date=trx_date, narration=narration,
                status=JOURNAL_ENTRY_STATUS.Posted, entry_type=entry_type
            )
        else:
            return GeneralJournal(
                created_by_id=user_id, coa_id=coa_id, partner_id=partner_id,
                is_credit=is_credit, amount=amount,
                trx_ref_number=trx_ref_number, trx_date=trx_date, narration=narration,
                status=JOURNAL_ENTRY_STATUS.Posted, entry_type=entry_type
            )


auditlog.register(ChartOfAccounts)
