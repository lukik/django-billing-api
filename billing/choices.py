__author__ = 'Muchai Noah'

from model_utils import Choices
from django.utils.translation import gettext_lazy as _


INVOICE_STATUS = Choices(
    (1, 'Draft', _('Draft')),
    (2, 'Unpaid', _('Unpaid')),
    (3, 'PartPayment', _('Part Payment')),
    (4, 'Paid', _('Paid')),
    (5, 'Cancelled', _('Cancelled'))
)

LINE_ITEM_STATUS = Choices(
    (1, 'Unpaid', _('Unpaid')),
    (2, 'PartPayment', _('Part Payment')),
    (3, 'Paid', _('Paid')),
    (4, 'Cancelled', _('Cancelled'))
)
INVOICE_DETAIL_TYPE = Choices(
    (1, 'LineItem', _('Line Item')),
    (2, 'Discount', _('Discount')),
    (3, 'Penalty', _('Penalty')),
    (4, 'Payment', _('Payment')),
)