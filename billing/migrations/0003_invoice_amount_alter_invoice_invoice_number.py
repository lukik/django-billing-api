# Generated by Django 4.1.1 on 2022-09-25 15:31

import billing.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("billing", "0002_invoice_invoicedetail"),
    ]

    operations = [
        migrations.AddField(
            model_name="invoice",
            name="amount",
            field=models.DecimalField(decimal_places=2, default=1, max_digits=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="invoice",
            name="invoice_number",
            field=models.IntegerField(
                default=billing.models.generate_invoice_number, unique=True
            ),
        ),
    ]
