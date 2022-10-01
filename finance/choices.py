__author__ = 'Muchai Noah'

from model_utils import Choices
from django.utils.translation import gettext_lazy as _


# Types of accounts in accounting
COA_TYPE = Choices(
    (1, 'Asset', _('Asset')),
    (2, 'Liability', _('Liability')),
    (3, 'Equity', _('Equity')),
    (4, 'Income', _('Income')),
    (5, 'Expense', _('Expense')),
)
# Status of a Journal Entry
JOURNAL_ENTRY_STATUS = Choices(
    (1, 'Posted', _('Posted')),
    (2, 'Reversed', _('Reversed')),
)
JOURNAL_ENTRY_TYPE = Choices(
    (1, 'SystemEntry', _('System Entry')),
    (2, 'ManualEntry', _('Manual Posting')),
)