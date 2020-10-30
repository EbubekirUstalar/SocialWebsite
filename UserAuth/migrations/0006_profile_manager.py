# Generated by Django 3.1.2 on 2020-10-30 17:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('UserAuth', '0005_auto_20201030_1834'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='manager',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employee', to='UserAuth.profile'),
        ),
    ]
