# Generated by Django 3.2.5 on 2021-08-03 06:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='profile',
            new_name='photo',
        ),
    ]
