from django.shortcuts import render

from django.shortcuts import render
from core.views import DeleteViewSet, ListCreateRetrieveUpdateViewSet
from partners.models import Partner
from partners.serializer import PartnerSerializer


class PartnerViewSet(DeleteViewSet, ListCreateRetrieveUpdateViewSet):
    """
    """
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer
    filter_fields = ('id', 'status')

