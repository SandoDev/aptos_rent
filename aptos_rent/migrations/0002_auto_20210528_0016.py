# Generated by Django 3.2.3 on 2021-05-28 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aptos_rent', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aptos',
            name='final_score',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='aptos',
            name='observations',
            field=models.TextField(blank=True, null=True),
        ),
    ]
