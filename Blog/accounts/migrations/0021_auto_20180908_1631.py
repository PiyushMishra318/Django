# Generated by Django 2.0.7 on 2018-09-08 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0020_auto_20180901_1216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.CharField(default='', max_length=100),
        ),
    ]
