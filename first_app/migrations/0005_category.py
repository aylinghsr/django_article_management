# Generated by Django 3.1 on 2021-03-08 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0004_auto_20210308_2210'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان دسته بندی')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='آدرس دسته بندی')),
                ('status', models.BooleanField(default=True, verbose_name='آیا نمایش داده شود؟')),
                ('position', models.IntegerField(verbose_name='پوزیشن')),
            ],
            options={
                'verbose_name': 'دسته بندی',
                'verbose_name_plural': 'دسته بندی ها',
                'ordering': ['position'],
            },
        ),
    ]
