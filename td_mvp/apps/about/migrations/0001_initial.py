# Generated by Django 4.2.5 on 2023-11-01 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Название')),
                ('value', models.CharField(max_length=64, verbose_name='Значение')),
                ('position', models.PositiveSmallIntegerField(default=0, verbose_name='Позиция')),
            ],
            options={
                'verbose_name': 'Реквизиты',
                'verbose_name_plural': 'Реквизит',
                'ordering': ['position'],
            },
        ),
        migrations.CreateModel(
            name='Geo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.IntegerField()),
                ('log', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Геопозиции',
                'verbose_name_plural': 'Геопозиция',
            },
        ),
    ]