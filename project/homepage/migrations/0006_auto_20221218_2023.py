# Generated by Django 3.2.16 on 2022-12-18 15:23

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('homepage', '0005_auto_20221215_2021'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category',
            new_name='ProgLanguage',
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'default_related_name': 'posts', 'verbose_name': 'пост', 'verbose_name_plural': 'посты'},
        ),
        migrations.RemoveField(
            model_name='post',
            name='category',
        ),
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
        migrations.AddField(
            model_name='post',
            name='code',
            field=models.TextField(blank=True, verbose_name='код'),
        ),
        migrations.AddField(
            model_name='post',
            name='prog_language',
            field=models.ForeignKey(help_text='ЯП', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='posts', to='homepage.proglanguage', verbose_name='язык программирования'),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(default=1, help_text='автор комментария', on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL, verbose_name='автор'),
        ),
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(help_text='Теги поста', related_name='posts', to='homepage.Tag', verbose_name='теги'),
        ),
    ]