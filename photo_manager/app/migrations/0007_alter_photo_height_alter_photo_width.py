# Generated by Django 4.1.2 on 2022-10-26 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0006_alter_photo_height_alter_photo_image_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="photo",
            name="height",
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="photo",
            name="width",
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
