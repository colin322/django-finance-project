# Generated by Django 5.1.4 on 2024-12-13 09:06

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0004_remove_userinfo_goals_goals_transactions'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Goals',
            new_name='Goal',
        ),
        migrations.RenameModel(
            old_name='Transactions',
            new_name='Transaction',
        ),
    ]