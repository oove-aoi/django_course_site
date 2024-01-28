# Generated by Django 4.2.4 on 2024-01-22 13:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("posts", "0006_alter_post_post_time"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="classification",
            field=models.CharField(
                choices=[("LR", "生活紀錄"), ("CR", "創作")], default="LR", max_length=2
            ),
        ),
        migrations.AddField(
            model_name="post",
            name="watchpeoplecount",
            field=models.SmallIntegerField(default=0),
        ),
    ]
