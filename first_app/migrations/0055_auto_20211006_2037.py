# Generated by Django 3.1 on 2021-10-06 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0054_auto_20211006_2034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='status',
            field=models.CharField(choices=[('p', 'منتشر شده'), ('b', 'برگشت داده شده'), ('i', 'در حال بررسی'), ('d', 'پیش نویس')], max_length=1, verbose_name='وضعیت'),
        ),
    ]
