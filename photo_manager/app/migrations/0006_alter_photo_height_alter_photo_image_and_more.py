# Generated by Django 4.1.2 on 2022-10-26 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0005_alter_photo_album_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="photo",
            name="height",
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name="photo",
            name="image",
            field=models.ImageField(
                height_field="height", upload_to="photos", width_field="width"
            ),
        ),
        migrations.AlterField(
            model_name="photo",
            name="width",
            field=models.PositiveIntegerField(),
        ),
    ]
