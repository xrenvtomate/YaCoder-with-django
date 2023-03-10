# Generated by Django 3.2.16 on 2022-12-22 15:50

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('homepage', '0013_auto_20221222_2039'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='age_of_post',
        ),
        migrations.RemoveField(
            model_name='post',
            name='is_published',
        ),
        migrations.RemoveField(
            model_name='proglanguage',
            name='is_published',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='is_published',
        ),
        migrations.AlterField(
            model_name='post',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, help_text='datetime of post creation', verbose_name='created on'),
        ),
        migrations.AlterField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(default=0, related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='popularity',
            field=models.FloatField(blank=True, default=0, help_text="post popularity = views / time since it's creation", verbose_name='popularity'),
        ),
        migrations.AlterField(
            model_name='post',
            name='views',
            field=models.PositiveIntegerField(blank=True, default=0, verbose_name='views'),
        ),
    ]
