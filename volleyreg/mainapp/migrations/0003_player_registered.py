# Generated by Django 2.2.1 on 2019-05-14 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_auto_20190514_2325'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='registered',
            field=models.BooleanField(default=False, editable=False, verbose_name='Зарегестрирован'),
        ),
    ]
