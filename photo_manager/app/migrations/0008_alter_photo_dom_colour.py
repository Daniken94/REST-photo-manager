# Generated by Django 4.1.2 on 2022-10-27 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0007_alter_photo_height_alter_photo_width"),
    ]

    operations = [
        migrations.AlterField(
            model_name="photo",
            name="dom_colour",
            field=models.CharField(blank=True, max_length=80),
        ),
    ]
