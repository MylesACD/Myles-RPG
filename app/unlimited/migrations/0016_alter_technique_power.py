# Generated by Django 4.1.3 on 2023-01-10 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("unlimited", "0015_technique_power_alter_technique_multitarget"),
    ]

    operations = [
        migrations.AlterField(
            model_name="technique",
            name="power",
            field=models.IntegerField(default=0, null=True),
        ),
    ]
