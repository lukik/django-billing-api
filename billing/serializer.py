from rest_framework import serializers
from core.serializer import CurrentUserSerializer
from billing.models import FeeItem, FeeStructure, Invoice


class FeeItemSerializer(CurrentUserSerializer):
    """Serialize model"""
    coa_name = serializers.ReadOnlyField(source='coa.title')

    class Meta:
        model = FeeItem
        fields = (
            'id', 'created_by', 'title', 'description',
            'coa', 'coa_name', 'display_sequence', 'is_active'
        )


class FeeStructureSerializer(CurrentUserSerializer):
    """Serialize model"""
    fee_item_name = serializers.ReadOnlyField(source='fee_item.title')
    last_updated = serializers.ReadOnlyField(source='modified_on')

    class Meta:
        model = FeeStructure
        fields = (
            'id', 'created_by', 'fee_item', 'amount',
            'fee_item_name', 'last_updated'
        )


class InvoiceSerializer(CurrentUserSerializer):
    """Serialize model"""
    partner_name = serializers.ReadOnlyField(source='partner.title')
    status_name = serializers.SerializerMethodField()

    def get_status_name(self, obj):
        return obj.get_status_display()

    class Meta:
        model = Invoice
        fields = (
            'id', 'created_by', 'partner', 'invoice_number', 'amount', 'invoice_date',
            'due_date', 'terms', 'status', 'status_date',
            'partner_name', 'status_name'
        )
        extra_kwargs = {
            'status_date': {'read_only': True},
            'invoice_number': {'read_only': True},
        }
