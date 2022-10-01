__author__ = 'Muchai Noah'

from model_utils import Choices
from django.utils.translation import gettext_lazy as _

PARTNER_STATUS = Choices(
    (1, 'Active', _('Active')),
    (2, 'Archived', _('Archived')),
    (3, 'Suspended', _('Suspended')),
    (4, 'Banned', _('Banned')),
    (5, 'Cancelled', _('Cancelled'))
)


