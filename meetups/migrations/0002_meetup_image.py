# Generated by Django 4.2.4 on 2023-12-29 17:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("meetups", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="meetup",
            name="image",
            field=models.ImageField(default="test", upload_to="images"),
            preserve_default=False,
        ),
    ]
