# Generated by Django 2.0.5 on 2018-06-08 19:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0012_auto_20180609_0350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='published_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
