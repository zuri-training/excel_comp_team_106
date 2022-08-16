# Generated by Django 4.1 on 2022-08-12 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_remove_file_file_remove_file_title_file_file_one_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Excel_doc_one',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_one', models.FileField(default='abc', upload_to='media/excel')),
            ],
        ),
        migrations.CreateModel(
            name='Excel_doc_two',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_two', models.FileField(default='abc', upload_to='media/excel')),
            ],
        ),
        migrations.DeleteModel(
            name='File',
        ),
    ]