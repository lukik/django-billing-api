# Generated by Django 4.1.1 on 2022-09-25 15:31

from django.db import migrations, models
import partners.models


class Migration(migrations.Migration):

    dependencies = [
        ("partners", "0003_alter_partner_account_number_alter_partner_status_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="partner",
            name="account_number",
            field=models.CharField(
                default=partners.models.generate_account_number,
                help_text="Number to identify the partner account",
                max_length=6,
                unique=True,
            ),
        ),
    ]
