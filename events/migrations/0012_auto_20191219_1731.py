# Generated by Django 2.2.4 on 2019-12-19 12:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0011_auto_20191219_1709'),
    ]

    operations = [
        migrations.RenameField(
            model_name='speakerimg',
            old_name='title_key',
            new_name='slug',
        ),
    ]