# Generated by Django 4.1.3 on 2023-01-09 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("unlimited", "0012_alter_technique_area_alter_technique_range"),
    ]

    operations = [
        migrations.AlterField(
            model_name="technique",
            name="summon",
            field=models.CharField(
                choices=[(0, "NA"), (1, "1"), (2, "2"), (3, "3")],
                default=0,
                max_length=100,
            ),
        ),
    ]