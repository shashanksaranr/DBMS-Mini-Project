# Generated by Django 5.0.2 on 2024-03-09 14:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mini', '0025_alter_item_invoice_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Employee',
        ),
    ]