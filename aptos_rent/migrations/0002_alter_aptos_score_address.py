# Generated by Django 3.2.3 on 2021-05-27 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aptos_rent', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aptos',
            name='score_address',
            field=models.SmallIntegerField(choices=[(20, 'Jmmmm'), (40, 'Lejana'), (60, 'Pasable'), (80, 'Muy buena'), (90, 'Perfecta')]),
        ),
    ]