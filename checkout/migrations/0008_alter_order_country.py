# Generated by Django 4.2.13 on 2024-08-14 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0007_alter_order_postcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='country',
            field=models.CharField(blank=True, default='UK', max_length=40, null=True),
        ),
    ]
