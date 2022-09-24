from core.views import DeleteViewSet, ListCreateRetrieveUpdateViewSet
from billing.models import FeeItem, FeeStructure, Invoice
from billing.serializer import FeeItemSerializer, FeeStructureSerializer


class FeeItemViewSet(DeleteViewSet, ListCreateRetrieveUpdateViewSet):
    """
    Manage business fee items (i.e. items that a client can pay for)
    """
    queryset = FeeItem.objects.all()
    serializer_class = FeeItemSerializer
    filter_fields = ('id', 'coa', 'is_active')


class FeeStructureViewSet(DeleteViewSet, ListCreateRetrieveUpdateViewSet):
    """
    Manage business fee structure. i.e. how much to charge
    """
    queryset = FeeStructure.objects.all()
    serializer_class = FeeStructureSerializer
    filter_fields = ('id', 'fee_item')

