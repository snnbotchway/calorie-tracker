# Generated by Django 4.2.2 on 2023-06-13 10:18

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        (
            "tracker",
            "0004_rename_is_below_daily_calories_threshold_entry_below_daily_threshold",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="entry",
            name="below_daily_threshold",
            field=models.BooleanField(
                default=True,
                help_text=(
                    "Indicates if this entry causes the assigned user's total calories for the day"
                    " to be equal to or exceed their expected daily calories"
                ),
            ),
        ),
        migrations.AlterField(
            model_name="entry",
            name="calories",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                help_text="The number of calories in the meal(s)",
                max_digits=10,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="entry",
            name="date",
            field=models.DateField(auto_now_add=True, help_text="The date of the entry"),
        ),
        migrations.AlterField(
            model_name="entry",
            name="text",
            field=models.TextField(
                help_text=(
                    "The description of the meal(s) taken. Please prefix each meal with the"
                    " quantity of any measurement."
                )
            ),
        ),
        migrations.AlterField(
            model_name="entry",
            name="time",
            field=models.TimeField(auto_now_add=True, help_text="The time of the entry"),
        ),
        migrations.AlterField(
            model_name="entry",
            name="user",
            field=models.ForeignKey(
                help_text="The user associated with this entry",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="entries",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
