# Generated by Django 3.2.3 on 2021-06-15 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aptos_rent', '0005_aptos_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='aptos',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]