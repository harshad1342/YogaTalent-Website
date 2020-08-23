# Generated by Django 3.0.4 on 2020-04-16 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blog', '0002_delete_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=500)),
                ('content', models.TextField()),
                ('slug', models.CharField(max_length=150)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]
