# Generated by Django 2.0.2 on 2018-02-21 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='author',
            field=models.ForeignKey(on_delete=False, related_name='related_entries', to='authors.Author'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='entry',
            name='metadata',
            field=models.TextField(blank=True, null=True),
        ),
    ]
