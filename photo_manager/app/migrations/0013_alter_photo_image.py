# Generated by Django 4.1.2 on 2022-10-27 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0012_rename_albumid_photo_albumid"),
    ]

    operations = [
        migrations.AlterField(
            model_name="photo",
            name="image",
            field=models.ImageField(
                blank=True,
                height_field="height",
                null=True,
                upload_to="photos",
                width_field="width",
            ),
        ),
    ]
