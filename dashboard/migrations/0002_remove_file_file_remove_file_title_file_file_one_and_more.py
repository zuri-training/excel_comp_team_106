# Generated by Django 4.1 on 2022-08-11 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='file',
        ),
        migrations.RemoveField(
            model_name='file',
            name='title',
        ),
        migrations.AddField(
            model_name='file',
            name='file_one',
            field=models.FileField(default='abc', upload_to='media'),
        ),
        migrations.AddField(
            model_name='file',
            name='file_two',
            field=models.FileField(default='abc', upload_to='media'),
        ),
    ]
