# Generated by Django 2.0.2 on 2018-02-28 11:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='firstname',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='author',
            old_name='lastname',
            new_name='last_name',
        ),
    ]
