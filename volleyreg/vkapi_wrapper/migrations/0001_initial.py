# Generated by Django 2.2.1 on 2019-05-16 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Key',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True, verbose_name='Название')),
                ('key', models.CharField(max_length=256, verbose_name='Ключ')),
            ],
            options={
                'verbose_name': 'Ключ',
                'verbose_name_plural': 'Ключи',
            },
        ),
    ]
