# Generated by Django 5.1 on 2024-08-18 20:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_emoji_fontawesome_classname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='emoji',
            old_name='emojis',
            new_name='project',
        ),
    ]
