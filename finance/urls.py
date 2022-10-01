from rest_framework.routers import DefaultRouter

from finance.views import ChartOfAccountsViewSet, GeneralJournalViewSet

finance_router = DefaultRouter()

finance_router.register(r'coa', ChartOfAccountsViewSet)
finance_router.register(r'general-journal', GeneralJournalViewSet)
