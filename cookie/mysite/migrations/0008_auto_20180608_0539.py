# Generated by Django 2.0.5 on 2018-06-08 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0007_qa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='banner_image',
            field=models.CharField(max_length=50),
        ),
    ]
