# Generated by Django 4.1.2 on 2022-10-27 16:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0009_rename_album_id_photo_albumid_photo_url"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="photo",
            name="url",
        ),
    ]
