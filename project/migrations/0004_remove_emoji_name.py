# Generated by Django 5.1 on 2024-08-18 20:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_rename_emojis_emoji_project'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emoji',
            name='name',
        ),
    ]
