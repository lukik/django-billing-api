# Generated by Django 4.1.1 on 2022-09-24 14:56

import core.utils
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("partners", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="ChartOfAccounts",
            fields=[
                ("created_on", models.DateTimeField(auto_now_add=True)),
                ("modified_on", models.DateTimeField(auto_now=True)),
                (
                    "id",
                    models.UUIDField(
                        default=core.utils.get_uuid,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "coa_type",
                    models.PositiveSmallIntegerField(
                        choices=[
                            (1, "Asset"),
                            (2, "Liability"),
                            (3, "Equity"),
                            (4, "Income"),
                            (5, "Expense"),
                        ]
                    ),
                ),
                ("account_code", models.CharField(max_length=30, unique=True)),
                ("title", models.CharField(max_length=50, verbose_name="Account Name")),
                (
                    "description",
                    models.CharField(
                        max_length=200, verbose_name="Account Description"
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        editable=False,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="%(app_label)s_%(class)s_created_by",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "parent_account",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="finance.chartofaccounts",
                    ),
                ),
            ],
            options={
                "ordering": ("coa_type", "account_code"),
            },
        ),
        migrations.CreateModel(
            name="GeneralJournal",
            fields=[
                ("created_on", models.DateTimeField(auto_now_add=True)),
                ("modified_on", models.DateTimeField(auto_now=True)),
                (
                    "id",
                    models.UUIDField(
                        default=core.utils.get_uuid,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "amount",
                    models.DecimalField(
                        decimal_places=2, help_text="Amount transacted", max_digits=20
                    ),
                ),
                (
                    "trx_ref_number",
                    models.CharField(
                        blank=True,
                        help_text="Transaction reference number",
                        max_length=50,
                    ),
                ),
                (
                    "trx_date",
                    models.DateTimeField(
                        help_text="Date the customer made the transaction"
                    ),
                ),
                (
                    "is_credit",
                    models.BooleanField(help_text="True = Is Credit, False = Debit"),
                ),
                (
                    "narration",
                    models.CharField(
                        help_text="Specific narration for each transaction",
                        max_length=200,
                    ),
                ),
                (
                    "status",
                    models.PositiveSmallIntegerField(
                        choices=[(1, "Posted"), (2, "Reversed")],
                        default=1,
                        help_text="Entry status e.g. Valid, Posted etc",
                    ),
                ),
                (
                    "entry_type",
                    models.PositiveSmallIntegerField(
                        choices=[(1, "System Entry"), (2, "Manual Posting")],
                        default=1,
                        help_text="Entry by person or by the system?",
                    ),
                ),
                (
                    "coa",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="finance.chartofaccounts",
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        editable=False,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="%(app_label)s_%(class)s_created_by",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "partner",
                    models.ForeignKey(
                        help_text="Entity linked to the transaction",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="partners.partner",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
