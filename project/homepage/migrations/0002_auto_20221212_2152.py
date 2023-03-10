# Generated by Django 3.2.16 on 2022-12-12 16:52

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'default_related_name': 'items', 'verbose_name': 'пост', 'verbose_name_plural': 'посты'},
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(help_text='Категория поста', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='homepage.category', verbose_name='категория'),
        ),
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(help_text='Теги поста', related_name='items', to='homepage.Tag', verbose_name='теги'),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(blank=True, default='Sample Text', help_text='Описание поста', verbose_name='описание'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, max_length=500, verbose_name='комментарий')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='дата создания')),
                ('edited_on', models.DateTimeField(blank=True, null=True, verbose_name='дата изменения')),
                ('post', models.ForeignKey(help_text='пост, под которым находится комментарий', on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='homepage.post', verbose_name='пост')),
                ('prev_comment', models.ForeignKey(blank=True, help_text='комментарий, на который отвечает этот комментарий', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='homepage.comment', verbose_name='комментарий сверху')),
                ('user', models.ForeignKey(help_text='автор комментария', on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
            options={
                'verbose_name': 'комментарий',
                'verbose_name_plural': 'комментарии',
                'default_related_name': 'comments',
            },
        ),
    ]
