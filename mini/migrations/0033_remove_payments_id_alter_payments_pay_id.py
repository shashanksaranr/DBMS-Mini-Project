# Generated by Django 5.0.2 on 2024-03-13 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mini', '0032_alter_payments_account_no_alter_payments_bank_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payments',
            name='id',
        ),
        migrations.AlterField(
            model_name='payments',
            name='pay_id',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
