# Generated by Django 4.1.3 on 2023-03-30 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("unlimited", "0024_character_current_points_character_point_pool"),
    ]

    operations = [
        migrations.RenameField(
            model_name="technique", old_name="immobilizing", new_name="restricting",
        ),
        migrations.RemoveField(model_name="technique", name="armor_shred",),
        migrations.RemoveField(model_name="technique", name="cure",),
        migrations.RemoveField(model_name="technique", name="max_cost",),
        migrations.AddField(
            model_name="character",
            name="available_points",
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name="character",
            name="max_cost",
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name="technique",
            name="lasting",
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name="technique",
            name="area",
            field=models.CharField(
                choices=[
                    ("0", "none"),
                    ("1", "small"),
                    ("2", "medium"),
                    ("3", "large"),
                    ("4", "huge"),
                    ("5", "enormous"),
                    ("6", "colossal"),
                    ("7", "titanic"),
                ],
                default="0",
                max_length=100,
            ),
        ),
        migrations.AlterField(
            model_name="technique",
            name="forceful",
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="technique",
            name="range",
            field=models.CharField(
                choices=[
                    ("0", "close"),
                    ("1", "reach"),
                    ("2", "near"),
                    ("3", "far"),
                    ("4", "remote"),
                ],
                default="0",
                max_length=100,
            ),
        ),
    ]
