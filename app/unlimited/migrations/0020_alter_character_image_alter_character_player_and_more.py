# Generated by Django 4.1.3 on 2023-01-23 05:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("unlimited", "0019_alter_technique_boon"),
    ]

    operations = [
        migrations.AlterField(
            model_name="character",
            name="image",
            field=models.ImageField(blank=True, default="default.jpg", upload_to=""),
        ),
        migrations.AlterField(
            model_name="character",
            name="player",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AlterField(
            model_name="technique",
            name="author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AlterField(
            model_name="technique",
            name="character",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="unlimited.character",
            ),
        ),
    ]
