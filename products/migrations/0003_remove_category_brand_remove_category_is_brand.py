# Generated by Django 4.2.2 on 2023-07-03 16:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_category_brand_category_is_brand'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='category',
            name='is_brand',
        ),
    ]
