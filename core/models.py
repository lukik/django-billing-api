from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from core.utils import get_uuid


class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides self updating
    ``created`` and ``modified`` fields.
    """
    created_on = models.DateTimeField(auto_now_add=True, editable=False)
    modified_on = models.DateTimeField(auto_now=True, editable=False)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="%(app_label)s_%(class)s_created_by",
                                   editable=False, on_delete=models.PROTECT)

    class Meta:
        abstract = True


class BaseModel(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=get_uuid, editable=False)

    class Meta:
        abstract = True


class BaseModelNoID(TimeStampedModel):
    id = None

    class Meta:
        abstract = True