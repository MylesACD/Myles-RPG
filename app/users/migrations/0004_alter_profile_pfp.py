# Generated by Django 4.1.3 on 2023-01-24 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_alter_profile_pfp"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="pfp",
            field=models.ImageField(default="default.jpg", upload_to=""),
        ),
    ]
