# Generated by Django 2.0.5 on 2018-06-08 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0009_auto_20180608_0813'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='href',
            field=models.TextField(default='#'),
            preserve_default=False,
        ),
    ]