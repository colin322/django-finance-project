# Generated by Django 5.1.4 on 2024-12-16 13:13

import django.db.models.deletion
import tracker.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0006_rename_monthly_income_bruto_userinfo_monthly_income_netto_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SavingsAccountData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(default=2024)),
                ('months', models.JSONField(default=tracker.models.SavingsAccountData.get_default_months)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]