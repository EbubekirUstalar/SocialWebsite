# Generated by Django 3.1.2 on 2020-10-30 17:48

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('UserAuth', '0007_auto_20201030_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='manager',
            field=models.ManyToManyField(null=True, related_name='employee', to=settings.AUTH_USER_MODEL),
        ),
    ]
