# Generated by Django 4.2.2 on 2023-10-23 06:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_remove_purchase_payment_method'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchase',
            name='is_delivered',
        ),
        migrations.RemoveField(
            model_name='purchase',
            name='is_paid',
        ),
    ]
