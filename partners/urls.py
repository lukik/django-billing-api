from rest_framework.routers import DefaultRouter

from partners.views import PartnerViewSet, PartnerUploadViewSet

partner_router = DefaultRouter()

partner_router.register(r'bulk-upload', PartnerUploadViewSet)
partner_router.register(r'', PartnerViewSet)

