from rest_framework import serializers
from finance.models import ChartOfAccounts, GeneralJournal
from finance.choices import COA_TYPE, JOURNAL_ENTRY_STATUS, JOURNAL_ENTRY_TYPE


class ChartOfAccountsSerializer(serializers.ModelSerializer):
    """Serialize model"""
    coa_type = serializers.ChoiceField(choices=COA_TYPE)
    parent_account_code = serializers.ReadOnlyField(source='parent_account.account_code')
    parent_account_name = serializers.ReadOnlyField(source='parent_account.title')
    coa_type_name = serializers.SerializerMethodField()

    def get_coa_type_name(self, obj):
        return obj.get_coa_type_display()

    class Meta:
        model = ChartOfAccounts
        fields = ('id', 'coa_type', 'account_code', 'title', 'description', 'parent_account', 'parent_account_code',
                  'parent_account_name', 'coa_type_name')


class GeneralJournalSerializer(serializers.ModelSerializer):
    """Serialize model"""
    coa_name = serializers.CharField(source='coa.title', read_only=True)
    coa_number = serializers.CharField(source='coa.account_code', read_only=True)
    partner_name = serializers.ReadOnlyField(source='partner.partner_name')
    status_name = serializers.SerializerMethodField()
    entry_type_name = serializers.SerializerMethodField()
    coa_type_name = serializers.SerializerMethodField()
    entry_type = serializers.IntegerField(default=JOURNAL_ENTRY_TYPE.ManualEntry)

    def get_status_name(self, obj):
        return obj.get_status_display()

    def get_entry_type_name(self, obj):
        return obj.get_entry_type_display()

    def get_coa_type_name(self, obj):
        return COA_TYPE[obj.coa.coa_type]

    class Meta:
        model = GeneralJournal
        fields = ('id', 'coa', 'partner', 'amount', 'trx_ref_number', 'trx_date',
                  'is_credit', 'narration', 'status', 'entry_type',
                  'coa_name', 'coa_number', 'coa_type_name',
                  'partner_name', 'status_name', 'entry_type_name')
