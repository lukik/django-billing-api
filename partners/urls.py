from rest_framework.routers import DefaultRouter

from partners.views import PartnerViewSet

partner_router = DefaultRouter()

partner_router.register(r'', PartnerViewSet)
