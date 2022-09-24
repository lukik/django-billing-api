# Generated by Django 4.1.1 on 2022-09-24 19:10

import core.utils
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("partners", "0001_initial"),
        ("billing", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Invoice",
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
                ("invoice_number", models.IntegerField(unique=True)),
                ("invoice_date", models.DateTimeField(auto_now_add=True)),
                ("due_date", models.DateField(null=True)),
                ("terms", models.CharField(blank=True, max_length=250)),
                (
                    "status",
                    models.PositiveSmallIntegerField(
                        choices=[
                            (1, "Draft"),
                            (2, "Unpaid"),
                            (3, "Part Payment"),
                            (4, "Paid"),
                            (5, "Cancelled"),
                        ]
                    ),
                ),
                ("status_date", models.DateTimeField(auto_now=True)),
                ("status_by", models.UUIDField(help_text="Related User", null=True)),
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
                        on_delete=django.db.models.deletion.CASCADE,
                        to="partners.partner",
                    ),
                ),
            ],
            options={
                "ordering": ("-created_on",),
            },
        ),
        migrations.CreateModel(
            name="InvoiceDetail",
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
                    "detail_type",
                    models.PositiveSmallIntegerField(
                        choices=[
                            (1, "Line Item"),
                            (2, "Discount"),
                            (3, "Penalty"),
                            (4, "Payment"),
                        ]
                    ),
                ),
                (
                    "line_item_status",
                    models.PositiveSmallIntegerField(
                        choices=[
                            (1, "Unpaid"),
                            (2, "Part Payment"),
                            (3, "Paid"),
                            (4, "Cancelled"),
                        ],
                        help_text="Applies to items of Detail Type LineItem",
                        null=True,
                    ),
                ),
                ("line_item_status_date", models.DateTimeField(null=True)),
                ("amount", models.DecimalField(decimal_places=2, max_digits=20)),
                ("description", models.CharField(blank=True, max_length=250)),
                (
                    "trx_ref_number",
                    models.TextField(
                        blank=True, help_text="Code to identify the transaction"
                    ),
                ),
                ("trx_time", models.DateTimeField()),
                ("is_cancelled", models.BooleanField(default=False)),
                ("reason_cancelled", models.CharField(blank=True, max_length=100)),
                (
                    "cancelled_by",
                    models.UUIDField(
                        editable=False, help_text="Related User", null=True
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
                    "fee_item",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="fee_items",
                        to="billing.feeitem",
                    ),
                ),
                (
                    "invoice",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="invoice_details",
                        to="billing.invoice",
                    ),
                ),
                (
                    "line_item",
                    models.ForeignKey(
                        help_text="The line item the entry is related to",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="line_items",
                        to="billing.invoicedetail",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]