# Generated by Django 3.2.16 on 2022-12-12 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_auto_20221212_2152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='edited_on',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='дата изменения'),
        ),
    ]
