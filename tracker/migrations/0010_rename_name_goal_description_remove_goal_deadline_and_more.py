# Generated by Django 5.1.4 on 2025-01-08 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0009_remove_userinfo_monthly_expenses'),
    ]

    operations = [
        migrations.RenameField(
            model_name='goal',
            old_name='name',
            new_name='description',
        ),
        migrations.RemoveField(
            model_name='goal',
            name='deadline',
        ),
        migrations.RemoveField(
            model_name='goal',
            name='saved_amount',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='monthly_budget',
        ),
        migrations.AddField(
            model_name='goal',
            name='monthly_budget',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
