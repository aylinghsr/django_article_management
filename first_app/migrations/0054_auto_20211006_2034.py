# Generated by Django 3.1 on 2021-10-06 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0053_auto_20211005_2213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='status',
            field=models.CharField(choices=[('b', 'برگشت داده شده'), ('d', 'پیش نویس'), ('p', 'منتشر شده'), ('i', 'در حال بررسی')], max_length=1, verbose_name='وضعیت'),
        ),
    ]
