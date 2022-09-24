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
