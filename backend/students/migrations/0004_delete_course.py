# Generated by Django 5.2.3 on 2025-06-13 07:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_rename_paymentreceipt_payment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Course',
        ),
    ]
