# Generated by Django 4.1.3 on 2023-01-28 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("unlimited", "0020_alter_character_image_alter_character_player_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="technique",
            name="subtle",
            field=models.BooleanField(default=False),
        ),
    ]
