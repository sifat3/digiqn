# Generated by Django 4.2.7 on 2024-01-25 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_request_transaction_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='transaction_id',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
