# Generated by Django 3.0.4 on 2020-04-17 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20200418_0036'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='benefit',
            field=models.TextField(default=122),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='post',
            name='steps',
            field=models.TextField(),
        ),
    ]
