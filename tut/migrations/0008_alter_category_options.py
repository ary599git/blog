# Generated by Django 3.2.5 on 2021-09-28 18:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tut', '0007_alter_category_parent'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['parent__id', 'position'], 'verbose_name': 'دسته بندی', 'verbose_name_plural': 'دسته بندی ها'},
        ),
    ]