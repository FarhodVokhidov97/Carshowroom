# Generated by Django 4.1.4 on 2023-02-25 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0013_spare_part_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='spare_part',
            name='slug',
            field=models.SlugField(default=1),
            preserve_default=False,
        ),
    ]
