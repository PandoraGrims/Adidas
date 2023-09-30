# Generated by Django 4.2.2 on 2023-09-27 10:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_remove_product_category_product_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='imgs', verbose_name='Изображение')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='webapp.product', verbose_name='Продукт')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ManyToManyField(blank=True, related_name='products', to='webapp.productimage', verbose_name='Изображения'),
        ),
    ]