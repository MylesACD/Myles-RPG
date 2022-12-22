# Generated by Django 4.1.3 on 2022-12-15 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "unlimited",
            "0008_technique_combo_technique_controlled_technique_cure_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="technique",
            name="armor_shred",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="technique",
            name="practiced",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="technique",
            name="stunning",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="technique",
            name="summon",
            field=models.CharField(
                choices=[("0", "0"), ("1", "1"), ("2", "2"), ("3", "3")],
                default="0",
                max_length=100,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="technique",
            name="terrain",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="technique",
            name="transformation",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="technique",
            name="vampiric",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="technique",
            name="heal",
            field=models.CharField(
                choices=[("0", "0%"), ("1", "50%"), ("2", "100%")],
                default="0%",
                max_length=100,
                null=True,
            ),
        ),
    ]
