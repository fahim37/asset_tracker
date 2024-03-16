# Generated by Django 5.0.3 on 2024-03-16 06:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("account", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Device",
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
                ("device_type", models.CharField(max_length=255)),
                ("serial_number", models.CharField(max_length=255, unique=True)),
                ("condition_on_checkout", models.TextField(blank=True)),
                ("checked_out", models.BooleanField(default=False)),
                (
                    "company",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="account.company",
                    ),
                ),
            ],
        ),
    ]
