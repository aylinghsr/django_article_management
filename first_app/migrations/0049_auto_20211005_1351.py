# Generated by Django 3.1 on 2021-10-05 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0048_auto_20211005_1339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='status',
            field=models.CharField(choices=[('d', 'پیش نویس'), ('i', 'در حال بررسی'), ('b', 'برگشت داده شده'), ('p', 'منتشر شده')], max_length=1, verbose_name='وضعیت'),
        ),
    ]
