from core.views import DeleteViewSet, ListCreateRetrieveUpdateViewSet, ListCreateRetrieveViewSet
from partners.serializer import PartnerSerializer
from finance.models import ChartOfAccounts, GeneralJournal
from finance.serializer import ChartOfAccountsSerializer, GeneralJournalSerializer


class ChartOfAccountsViewSet(DeleteViewSet, ListCreateRetrieveUpdateViewSet):
    """
    Manage Chart of Accounts (COA)
    """
    queryset = ChartOfAccounts.objects.all()
    serializer_class = ChartOfAccountsSerializer
    filter_fields = ('id', 'coa_type', 'account_code', 'parent_account')
    search_fields = ['account_code', 'title']
    ordering = ('account_code',)


class GeneralJournalViewSet(ListCreateRetrieveViewSet):
    """
    Manage general journal entries
    """
    queryset = GeneralJournal.objects.all()
    serializer_class = GeneralJournalSerializer
    filter_fields = ('id', 'coa', 'partner', 'trx_ref_number', 'entry_type')
