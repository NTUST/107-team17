# Generated by Django 2.0.5 on 2018-06-08 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0013_auto_20180609_0356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='href',
            field=models.TextField(default='#'),
        ),
    ]
