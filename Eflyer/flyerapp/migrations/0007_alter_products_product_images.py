# Generated by Django 4.2.6 on 2023-12-01 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flyerapp', '0006_alter_products_product_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='product_images',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
