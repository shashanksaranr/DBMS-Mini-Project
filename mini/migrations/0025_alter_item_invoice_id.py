# Generated by Django 5.0.2 on 2024-03-01 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mini', '0024_alter_item_invoice_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='invoice_id',
            field=models.IntegerField(),
        ),
    ]
