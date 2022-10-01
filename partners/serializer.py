import os
from rest_framework import serializers
from core.serializer import CurrentUserSerializer
from core.api_exceptions import InvalidFileName
from partners.models import Partner, PartnerUpload
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
        fields = (
            'id', 'created_by', 'title', 'account_number',
            'status', 'status_name', 'is_client', 'is_supplier'
        )


class PartnerUploadSerializer(CurrentUserSerializer):
    """Serialize model"""
    file = serializers.FileField(use_url=True, source='document')
    upload_date = serializers.ReadOnlyField()
    file_name = serializers.ReadOnlyField()

    class Meta:
        model = PartnerUpload
        fields = (
            'id', 'created_by', 'file', 'upload_date',
            'imported_successfully', 'import_summary', 'file_name',
        )
        extra_kwargs = {
            'imported_successfully': {'read_only': True},
            'import_summary': {'read_only': True},
        }

    def validate(self, attrs):

        ext = os.path.splitext(attrs['document'].name)[1]
        if ext != ".csv":
            raise InvalidFileName("Invalid File Type. Only .csv files are allowed")

        attrs['file_name'] = os.path.splitext(attrs['document'].name)[0]

        return attrs
