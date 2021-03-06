# Generated by Django 3.0.7 on 2020-06-19 21:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Тэг')),
            ],
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Тема')),
            ],
        ),
        migrations.CreateModel(
            name='IdeaOffer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme', models.CharField(max_length=511, verbose_name='Тема идеи')),
                ('description', models.TextField(verbose_name='Подробное описание идеи')),
                ('tags', models.ManyToManyField(null=True, to='ideas.Tag', verbose_name='Тэги')),
                ('themes', models.ManyToManyField(to='ideas.Theme', verbose_name='Темы')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Инициатор идеи')),
            ],
        ),
        migrations.CreateModel(
            name='IdeaLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ideas.IdeaOffer', verbose_name='Идея')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Лайкнувший')),
            ],
        ),
        migrations.CreateModel(
            name='IdeaComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(verbose_name='Текст комментария')),
                ('idea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ideas.IdeaOffer', verbose_name='Идея')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Коментатор')),
            ],
        ),
    ]
