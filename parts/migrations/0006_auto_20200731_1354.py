# Generated by Django 3.0.6 on 2020-07-31 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parts', '0005_auto_20200727_1229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bike_models',
            name='model_name',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='body_types',
            name='body_name',
            field=models.CharField(choices=[('sport', 'Sport'), ('touring', 'Touring'), ('standard', 'Standard'), ('cruiser', 'Cruiser'), ('dual-purpose', 'Dual-Purpose'), ('dirt_bike', 'Dirt Bike'), ('others', 'Others')], default='others', max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='brands',
            name='brand_name',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='parts_categories',
            name='category_name',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='subcategories',
            name='title',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]