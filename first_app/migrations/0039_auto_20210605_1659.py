# Generated by Django 3.1 on 2021-06-05 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0038_auto_20210605_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='status',
            field=models.CharField(choices=[('d', 'پیش نویس'), ('b', 'برگشت داده شده'), ('p', 'منتشر شده'), ('i', 'در حال بررسی')], max_length=1, verbose_name='وضعیت'),
        ),
    ]