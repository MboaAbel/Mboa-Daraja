# Generated by Django 3.0.5 on 2023-11-12 18:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_userbankaccount_mboacoins_balance'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userbankaccount',
            name='MboaCoins_Balance',
        ),
    ]
