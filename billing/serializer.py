from rest_framework import serializers
from billing.models import FeeItem, FeeStructure, Invoice
from billing.choices import INVOICE_STATUS, LINE_ITEM_STATUS, INVOICE_DETAIL_TYPE


class FeeItemSerializer(serializers.ModelSerializer):
    """Serialize model"""
    coa_name = serializers.ReadOnlyField(source='coa.title')

    class Meta:
        model = FeeItem
        fields = ('id', 'title', 'description', 'coa', 'coa_name', 'display_sequence', 'is_active')


class FeeStructureSerializer(serializers.ModelSerializer):
    """Serialize model"""
    fee_item_name = serializers.ReadOnlyField(source='fee_item.title')
    last_updated = serializers.ReadOnlyField(source='modified_on')

    class Meta:
        model = FeeStructure
        fields = ('id', 'fee_item', 'amount', 'fee_item_name', 'last_updated')
