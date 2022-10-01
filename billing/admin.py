from django.contrib import admin
from billing.models import FeeItem, FeeStructure


admin.site.register(FeeItem)
admin.site.register(FeeStructure)
