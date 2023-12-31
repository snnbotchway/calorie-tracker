# Generated by Django 4.2.2 on 2023-06-13 10:18

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("accounts", "0003_alter_usersettings_expected_daily_calories"),
    ]

    operations = [
        migrations.AlterField(
            model_name="usersettings",
            name="expected_daily_calories",
            field=models.DecimalField(
                decimal_places=2,
                default=2250,
                help_text="The expected number of calories a user aims to consume in a day.",
                max_digits=10,
            ),
        ),
        migrations.AlterField(
            model_name="usersettings",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="settings",
                to=settings.AUTH_USER_MODEL,
                verbose_name="user",
            ),
        ),
    ]
