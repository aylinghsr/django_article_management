# Generated by Django 3.1 on 2021-05-02 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0017_auto_20210502_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='status',
            field=models.CharField(choices=[('p', 'منتشر شده'), ('d', 'پیش نویس')], max_length=1, verbose_name='وضعیت'),
        ),
    ]
