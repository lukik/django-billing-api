from rest_framework.routers import DefaultRouter

from billing.views import FeeItemViewSet, FeeStructureViewSet, InvoiceViewSet

billing_router = DefaultRouter()

billing_router.register(r'fee-item', FeeItemViewSet)
billing_router.register(r'fee-structure', FeeStructureViewSet)
billing_router.register('invoice', InvoiceViewSet)
