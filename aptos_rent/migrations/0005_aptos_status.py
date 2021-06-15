# Generated by Django 3.2.3 on 2021-06-15 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aptos_rent', '0004_auto_20210614_2023'),
    ]

    operations = [
        migrations.AddField(
            model_name='aptos',
            name='status',
            field=models.CharField(choices=[('Not started', 'Not started'), ('In progress', 'In progress'), ('Finished', 'Finished')], default='Not started', max_length=11),
        ),
    ]
