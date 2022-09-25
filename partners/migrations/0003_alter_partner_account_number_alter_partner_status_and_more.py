# Generated by Django 4.1.1 on 2022-09-25 06:56

from django.db import migrations, models
import partners.models


class Migration(migrations.Migration):

    dependencies = [
        ("partners", "0002_partner_title"),
    ]

    operations = [
        migrations.AlterField(
            model_name="partner",
            name="account_number",
            field=models.CharField(
                default=partners.models.generate_account_number,
                help_text="Number to identify the partner account",
                max_length=5,
                unique=True,
            ),
        ),
        migrations.AlterField(
            model_name="partner",
            name="status",
            field=models.PositiveSmallIntegerField(
                choices=[
                    (1, "Active"),
                    (2, "Archived"),
                    (3, "Suspended"),
                    (4, "Banned"),
                    (5, "Cancelled"),
                ],
                default=1,
            ),
        ),
        migrations.AlterField(
            model_name="partner",
            name="title",
            field=models.CharField(
                help_text="Name to identify the partner account",
                max_length=100,
                unique=True,
            ),
        ),
    ]