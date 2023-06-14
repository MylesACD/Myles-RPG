# Generated by Django 4.1.3 on 2023-06-13 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("unlimited", "0032_alter_technique_content_alter_technique_piercing"),
    ]

    operations = [
        migrations.AddField(
            model_name="technique",
            name="adjustment",
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="technique",
            name="area",
            field=models.CharField(
                choices=[
                    ("0", "None"),
                    ("1", "Small"),
                    ("2", "Medium"),
                    ("3", "Large"),
                    ("4", "Huge"),
                    ("5", "Enormous"),
                    ("6", "Colossal"),
                    ("7", "Titanic"),
                ],
                default="0",
                max_length=100,
            ),
        ),
        migrations.AlterField(
            model_name="technique", name="cost", field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="technique",
            name="piercing",
            field=models.CharField(
                choices=[
                    ("0", "None"),
                    ("1", "Armor Piercing"),
                    ("2", "Armor Shredding"),
                ],
                default="0",
                max_length=100,
            ),
        ),
    ]
