# Generated by Django 3.0.7 on 2020-06-20 07:21

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ideas', '0007_auto_20200620_1721'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Solution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Создано')),
                ('modified', models.DateTimeField(auto_now=True, null=True, verbose_name='Изменено')),
                ('short_description', models.CharField(max_length=511, verbose_name='Краткое описание решения')),
                ('task', ckeditor.fields.RichTextField(verbose_name='Задача')),
                ('description', ckeditor.fields.RichTextField(verbose_name='Подробное описание')),
                ('result', ckeditor.fields.RichTextField(verbose_name='Результать')),
                ('resources', ckeditor.fields.RichTextField(verbose_name='Ресурсы')),
                ('price_min', models.DecimalField(decimal_places=2, max_digits=100, max_length=100, verbose_name='Стоимость реализации от')),
                ('price_max', models.DecimalField(decimal_places=2, max_digits=100, max_length=100, verbose_name='Стоимость реализации до')),
                ('idea', models.ForeignKey(blank=True, help_text='Если решение привязано к идее то это решение к идее.Если нет это предложение бизнес-решения.', null=True, on_delete=django.db.models.deletion.CASCADE, to='ideas.IdeaOffer', verbose_name='Решение')),
                ('tags', models.ManyToManyField(to='ideas.Tag', verbose_name='Тэги')),
                ('themes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ideas.Theme', verbose_name='Выбранная тема')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Инициатор решения')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]