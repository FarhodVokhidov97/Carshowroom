# Generated by Django 4.0.2 on 2022-12-11 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_product_image_product_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='year',
            field=models.IntegerField(default=12),
            preserve_default=False,
        ),
        migrations.AlterModelTable(
            name='category',
            table='Brand',
        ),
        migrations.AlterModelTable(
            name='product',
            table='Cars',
        ),
    ]
