# Generated by Django 4.1.4 on 2023-02-25 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_spare_category_spare_part'),
    ]

    operations = [
        migrations.AddField(
            model_name='spare_category',
            name='slug',
            field=models.SlugField(default=1),
            preserve_default=False,
        ),
    ]
