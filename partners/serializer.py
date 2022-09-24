from rest_framework import serializers
from partners.models import Partner
from partners.choices import PARTNER_STATUS


class PartnerSerializer(serializers.ModelSerializer):
    """Serialize model"""
    status = serializers.ChoiceField(choices=PARTNER_STATUS)
    status_name = serializers.SerializerMethodField()

    def get_status_name(self, obj):
        return obj.get_status_display()

    class Meta:
        model = Partner
        fields = ('id', 'title', 'status', 'status_name', 'is_client', 'is_supplier')
