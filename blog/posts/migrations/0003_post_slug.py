# Generated by Django 4.2.4 on 2024-01-11 12:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("posts", "0002_comment"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="slug",
            field=models.SlugField(default=""),
        ),
    ]
