# Generated by Django 2.0.5 on 2018-06-09 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0016_auto_20180609_2237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productdetail',
            name='calorie',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='productdetail',
            name='weight',
            field=models.CharField(max_length=50),
        ),
    ]