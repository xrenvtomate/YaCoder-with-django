# Generated by Django 3.2.16 on 2022-12-11 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20221211_1946'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(default='def_profile_pic.jpg', upload_to='images/%Y/%m', verbose_name='изображение профиля'),
        ),
    ]
