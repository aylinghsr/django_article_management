# Generated by Django 3.1 on 2021-03-06 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='status',
            field=models.CharField(choices=[('p', 'Published'), ('d', 'Draft')], max_length=1),
        ),
    ]
