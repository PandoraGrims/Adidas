# Generated by Django 4.2.2 on 2023-10-23 06:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_purchase'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchase',
            name='payment_method',
        ),
    ]
