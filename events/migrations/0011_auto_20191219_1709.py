# Generated by Django 2.2.4 on 2019-12-19 11:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0010_speakerimg_speaker_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='speakerimg',
            old_name='title',
            new_name='title_key',
        ),
    ]
