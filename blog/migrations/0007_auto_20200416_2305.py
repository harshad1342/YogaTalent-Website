# Generated by Django 3.0.4 on 2020-04-16 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20200416_2251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='blog/static/images'),
        ),
    ]