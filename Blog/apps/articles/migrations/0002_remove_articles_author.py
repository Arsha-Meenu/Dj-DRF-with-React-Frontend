# Generated by Django 4.2 on 2023-04-21 05:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articles',
            name='author',
        ),
    ]
