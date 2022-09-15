# Generated by Django 4.1 on 2022-09-15 11:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("forms", "0001_initial"),
        ("registrations", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="formanswer",
            name="kiosk_registration",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="registrations.kioskregistration",
            ),
        ),
    ]
