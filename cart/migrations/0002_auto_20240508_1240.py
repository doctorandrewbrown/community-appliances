# Generated by Django 3.2.24 on 2024-05-08 12:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderlineitem',
            name='product_size',
        ),
        migrations.RemoveField(
            model_name='orderlineitem',
            name='quantity',
        ),
    ]
