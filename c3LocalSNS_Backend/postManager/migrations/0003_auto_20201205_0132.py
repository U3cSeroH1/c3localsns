# Generated by Django 3.1.3 on 2020-12-04 16:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('postManager', '0002_auto_20201204_1126'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='authoricon',
            new_name='authoravatar',
        ),
    ]
