# Generated by Django 2.0.7 on 2018-08-17 07:26

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0003_auto_20180817_1254'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='username',
        ),
        migrations.AddField(
            model_name='post',
            name='username',
            field=models.ManyToManyField(default='', to=settings.AUTH_USER_MODEL),
        ),
    ]
