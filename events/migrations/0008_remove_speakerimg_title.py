# Generated by Django 2.2.4 on 2019-12-19 07:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_auto_20191219_1254'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='speakerimg',
            name='title',
        ),
    ]
