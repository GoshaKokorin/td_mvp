# Generated by Django 4.2.5 on 2023-11-01 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='geo',
            name='lat',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='geo',
            name='log',
            field=models.FloatField(),
        ),
    ]
