# Generated by Django 4.2.2 on 2023-11-05 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0009_purchase_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='is_paid',
            field=models.BooleanField(default=False, verbose_name='Оплачен'),
        ),
    ]
