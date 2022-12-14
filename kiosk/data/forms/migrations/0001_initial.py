# Generated by Django 4.1 on 2022-09-15 11:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="KioskForm",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="FormQuestion",
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
                ("title", models.CharField(max_length=64)),
                (
                    "question_type",
                    models.CharField(
                        choices=[
                            ("I", "Input"),
                            ("T", "textarea"),
                            ("S", "Select"),
                            ("C", "Checkbox"),
                        ],
                        default="I",
                        max_length=1,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "kiosk_form",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="forms.kioskform",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="FormAnswer",
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
                ("value", models.JSONField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "form_question",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="forms.kioskform",
                    ),
                ),
            ],
        ),
    ]
