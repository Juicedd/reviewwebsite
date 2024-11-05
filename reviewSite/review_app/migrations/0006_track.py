# Generated by Django 5.1 on 2024-10-31 20:59

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("review_app", "0005_rename_favorite_track_id_review_favorite_track_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Track",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=50)),
                (
                    "track_number",
                    models.IntegerField(
                        verbose_name=django.core.validators.MinValueValidator(1)
                    ),
                ),
                (
                    "album",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="review_app.album",
                    ),
                ),
            ],
        ),
    ]