# Generated by Django 4.1.2 on 2022-10-26 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0002_delete_test"),
    ]

    operations = [
        migrations.AddField(
            model_name="photo",
            name="image",
            field=models.ImageField(default=0, upload_to="photos"),
            preserve_default=False,
        ),
    ]
