# Generated by Django 4.1.3 on 2023-02-09 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("unlimited", "0023_alter_technique_mobile"),
    ]

    operations = [
        migrations.AddField(
            model_name="character",
            name="current_points",
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name="character",
            name="point_pool",
            field=models.IntegerField(null=True),
        ),
    ]
