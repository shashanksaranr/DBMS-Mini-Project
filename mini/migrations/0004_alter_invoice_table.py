# Generated by Django 5.0.2 on 2024-02-28 17:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mini', '0003_alter_invoice_cust_id_alter_invoice_due_date_and_more'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='invoice',
            table='invoices',
        ),
    ]
