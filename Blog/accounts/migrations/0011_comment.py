# Generated by Django 2.0.7 on 2018-08-30 07:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_remove_post_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_id', models.CharField(max_length=100)),
                ('text', models.CharField(default='', max_length=100)),
                ('date', models.DateField(default=datetime.datetime.today)),
            ],
        ),
    ]
