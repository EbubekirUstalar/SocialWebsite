# Generated by Django 3.1.2 on 2020-10-27 17:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UserAuth', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='header',
        ),
    ]