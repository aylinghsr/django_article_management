# Generated by Django 3.1 on 2021-03-31 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0013_auto_20210327_2133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='status',
            field=models.CharField(choices=[('d', 'پیش نویس'), ('p', 'منتشر شده')], max_length=1, verbose_name='وضعیت'),
        ),
    ]