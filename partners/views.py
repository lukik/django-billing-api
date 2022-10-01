from core.views import DeleteViewSet, ListCreateRetrieveUpdateViewSet
from partners.models import Partner, PartnerUpload
from partners.serializer import PartnerSerializer, PartnerUploadSerializer


class PartnerViewSet(DeleteViewSet, ListCreateRetrieveUpdateViewSet):
    """
    Manage partners of the business
    """
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer
    filter_fields = ('id', 'status', 'is_client', 'is_supplier')


class PartnerUploadViewSet(DeleteViewSet, ListCreateRetrieveUpdateViewSet):
    """
    Manage bulk importation of partners (upload a file)
    """
    queryset = PartnerUpload.objects.all()
    serializer_class = PartnerUploadSerializer
    filter_fields = ('id', 'upload_date', 'imported_successfully')

