# Generated by Django 4.1 on 2022-08-29 19:59

import data.users.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="kioskuser",
            managers=[
                ("objects", data.users.models.KioskUserManager()),
            ],
        ),
    ]
