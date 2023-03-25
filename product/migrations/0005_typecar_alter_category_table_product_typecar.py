# Generated by Django 4.0.2 on 2023-02-23 14:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_product_year_alter_category_table_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TypeCar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nametype', models.CharField(max_length=255)),
                ('slug', models.SlugField()),
            ],
            options={
                'db_table': 'Brands',
                'ordering': ('nametype',),
            },
        ),
        migrations.AlterModelTable(
            name='category',
            table='Category',
        ),
        migrations.AddField(
            model_name='product',
            name='typecar',
            field=models.ForeignKey(default=31, on_delete=django.db.models.deletion.CASCADE, related_name='type', to='product.typecar'),
            preserve_default=False,
        ),
    ]
