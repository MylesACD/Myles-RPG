# Generated by Django 4.1.3 on 2023-01-09 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("unlimited", "0013_alter_technique_summon"),
    ]

    operations = [
        migrations.AddField(
            model_name="technique", name="cost", field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name="technique",
            name="max_cost",
            field=models.IntegerField(null=True),
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
                ],
                default="0",
                max_length=100,
            ),
        ),
        migrations.AlterField(
            model_name="technique",
            name="heal",
            field=models.CharField(
                choices=[("0", "0%"), ("1", "50%"), ("2", "100%")],
                default="0",
                max_length=100,
            ),
        ),
        migrations.AlterField(
            model_name="technique",
            name="multitarget",
            field=models.CharField(
                choices=[("1", "1"), ("2", "2"), ("3", "3"), ("4", "4")],
                default="1",
                max_length=100,
            ),
        ),
        migrations.AlterField(
            model_name="technique",
            name="range",
            field=models.CharField(
                choices=[
                    ("0", "touch"),
                    ("1", "reach"),
                    ("2", "near"),
                    ("3", "far"),
                    ("4", "remote"),
                ],
                default="0",
                max_length=100,
            ),
        ),
        migrations.AlterField(
            model_name="technique",
            name="summon",
            field=models.CharField(
                choices=[("0", "NA"), ("1", "1"), ("2", "2"), ("3", "3")],
                default="0",
                max_length=100,
            ),
        ),
    ]
