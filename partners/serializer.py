from rest_framework import serializers
from core.serializer import CurrentUserSerializer
from partners.models import Partner
from partners.choices import PARTNER_STATUS


class PartnerSerializer(CurrentUserSerializer):
    """Serialize model"""
    status = serializers.ChoiceField(choices=PARTNER_STATUS)
    status_name = serializers.SerializerMethodField()
    account_number = serializers.ReadOnlyField()

    def get_status_name(self, obj):
        return obj.get_status_display()

    class Meta:
        model = Partner
        fields = ('id', 'created_by', 'title', 'account_number',
                  'status', 'status_name', 'is_client', 'is_supplier')
