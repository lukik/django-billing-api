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
