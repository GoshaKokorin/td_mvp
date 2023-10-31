# Generated by Django 4.2.5 on 2023-09-09 12:42

from django.db import migrations, models
import td_mvp.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Main',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('image', models.ImageField(upload_to=td_mvp.utils.image_upload_to, verbose_name='Изображение')),
                ('description', models.TextField(verbose_name='Описание')),
                ('link', models.CharField(max_length=255, verbose_name='Ссылка на страницу')),
                ('position', models.PositiveSmallIntegerField(default=0, verbose_name='Позиция')),
            ],
            options={
                'verbose_name': 'Слайдер',
                'verbose_name_plural': 'Слайдеры',
                'ordering': ['position'],
            },
        ),
    ]