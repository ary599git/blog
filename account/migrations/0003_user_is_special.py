# Generated by Django 3.2.10 on 2022-01-31 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20220106_1206'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_special',
            field=models.BooleanField(default=False, verbose_name='مقاله ویژه'),
        ),
    ]
