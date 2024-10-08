# Generated by Django 5.1 on 2024-08-24 06:23

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("screen_app", "0067_alter_fixturecleaningrecord_no_dust_on_fixture_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="StartUpCheckSheet",
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
                ("revision_no", models.IntegerField(verbose_name="Rev. No.")),
                (
                    "effective_date",
                    models.DateField(
                        blank=True,
                        default=django.utils.timezone.now,
                        verbose_name="Eff. Date",
                    ),
                ),
                (
                    "process_operation",
                    models.CharField(
                        choices=[
                            ("visual_inspection", "Visual Inspection"),
                            ("programming_testing", "Programming & Testing"),
                            ("function_testing", "Function Testing"),
                            ("adhesive_application", "Adhesive Application"),
                            ("conformal_coating", "Conformal Coating"),
                            ("housing", "Housing"),
                            ("e90fl", "E90FL"),
                            ("dr_beck_epoxy", "Dr. Beck Epoxy"),
                            ("final_testing", "Final Testing"),
                        ],
                        max_length=300,
                        verbose_name="PROCESS/OPERATION",
                    ),
                ),
                (
                    "min_skill_required",
                    models.CharField(
                        max_length=100, verbose_name="MIN. SKILL REQUIRED"
                    ),
                ),
                (
                    "month",
                    models.DateField(blank=True, default=django.utils.timezone.now),
                ),
                (
                    "checkpoint_1",
                    models.CharField(
                        choices=[("✔", "OK"), ("✘", "Not OK")],
                        max_length=6,
                        verbose_name="Check Point 1",
                    ),
                ),
                (
                    "checkpoint_2",
                    models.CharField(
                        choices=[("✔", "OK"), ("✘", "Not OK")],
                        max_length=6,
                        verbose_name="Check Point 2",
                    ),
                ),
                (
                    "checkpoint_3",
                    models.CharField(
                        choices=[("✔", "OK"), ("✘", "Not OK")],
                        max_length=6,
                        verbose_name="Check Point 3",
                    ),
                ),
                (
                    "checkpoint_4",
                    models.CharField(
                        choices=[("✔", "OK"), ("✘", "Not OK")],
                        max_length=6,
                        verbose_name="Check Point 4",
                    ),
                ),
                (
                    "checkpoint_5",
                    models.CharField(
                        choices=[("✔", "OK"), ("✘", "Not OK")],
                        max_length=6,
                        verbose_name="Check Point 5",
                    ),
                ),
                (
                    "checkpoint_6",
                    models.CharField(
                        choices=[("✔", "OK"), ("✘", "Not OK")],
                        max_length=6,
                        verbose_name="Check Point 6",
                    ),
                ),
                (
                    "checkpoint_7",
                    models.CharField(
                        choices=[("✔", "OK"), ("✘", "Not OK")],
                        max_length=6,
                        verbose_name="Check Point 7",
                    ),
                ),
                (
                    "checkpoint_8",
                    models.CharField(
                        choices=[("✔", "OK"), ("✘", "Not OK")],
                        max_length=6,
                        verbose_name="Check Point 8",
                    ),
                ),
                (
                    "checkpoint_9",
                    models.CharField(
                        choices=[("✔", "OK"), ("✘", "Not OK")],
                        max_length=6,
                        verbose_name="Check Point 9",
                    ),
                ),
                (
                    "checkpoint_10",
                    models.CharField(
                        choices=[("✔", "OK"), ("✘", "Not OK")],
                        max_length=6,
                        verbose_name="Check Point 10",
                    ),
                ),
                (
                    "checkpoint_11",
                    models.CharField(
                        choices=[("✔", "OK"), ("✘", "Not OK")],
                        max_length=6,
                        verbose_name="Check Point 11",
                    ),
                ),
                (
                    "checkpoint_12",
                    models.CharField(
                        choices=[("✔", "OK"), ("✘", "Not OK")],
                        max_length=6,
                        verbose_name="Check Point 12",
                    ),
                ),
                (
                    "checkpoint_13",
                    models.CharField(
                        choices=[("✔", "OK"), ("✘", "Not OK")],
                        max_length=6,
                        verbose_name="Check Point 13",
                    ),
                ),
                (
                    "checkpoint_14",
                    models.CharField(
                        choices=[("✔", "OK"), ("✘", "Not OK")],
                        max_length=6,
                        verbose_name="Check Point 14",
                    ),
                ),
                (
                    "checkpoint_15",
                    models.CharField(
                        choices=[("✔", "OK"), ("✘", "Not OK")],
                        max_length=6,
                        verbose_name="Check Point 15",
                    ),
                ),
                (
                    "checkpoint_16",
                    models.CharField(
                        choices=[("✔", "OK"), ("✘", "Not OK")],
                        max_length=6,
                        verbose_name="Check Point 16",
                    ),
                ),
                (
                    "checkpoint_17",
                    models.CharField(
                        choices=[("✔", "OK"), ("✘", "Not OK")],
                        max_length=6,
                        verbose_name="Check Point 17",
                    ),
                ),
                (
                    "checkpoint_18",
                    models.CharField(
                        choices=[("✔", "OK"), ("✘", "Not OK")],
                        max_length=6,
                        verbose_name="Check Point 18",
                    ),
                ),
                (
                    "checkpoint_19",
                    models.CharField(
                        choices=[("✔", "OK"), ("✘", "Not OK")],
                        max_length=6,
                        verbose_name="Check Point 19",
                    ),
                ),
                (
                    "checkpoint_20",
                    models.CharField(
                        choices=[("✔", "OK"), ("✘", "Not OK")],
                        max_length=6,
                        verbose_name="Check Point 20",
                    ),
                ),
                (
                    "checkpoint_21",
                    models.CharField(
                        choices=[("✔", "OK"), ("✘", "Not OK")],
                        max_length=6,
                        verbose_name="Check Point 21",
                    ),
                ),
                (
                    "checkpoint_22",
                    models.CharField(
                        choices=[("✔", "OK"), ("✘", "Not OK")],
                        max_length=6,
                        verbose_name="Check Point 22",
                    ),
                ),
                (
                    "checkpoint_23",
                    models.CharField(
                        choices=[("✔", "OK"), ("✘", "Not OK")],
                        max_length=6,
                        verbose_name="Check Point 23",
                    ),
                ),
                (
                    "checkpoint_24",
                    models.CharField(
                        choices=[("✔", "OK"), ("✘", "Not OK")],
                        max_length=6,
                        verbose_name="Check Point 24",
                    ),
                ),
                (
                    "checkpoint_25",
                    models.CharField(
                        choices=[("✔", "OK"), ("✘", "Not OK")],
                        max_length=6,
                        verbose_name="Check Point 25",
                    ),
                ),
                (
                    "checkpoint_26",
                    models.CharField(
                        choices=[("✔", "OK"), ("✘", "Not OK")],
                        max_length=6,
                        verbose_name="Check Point 26",
                    ),
                ),
                (
                    "checkpoint_27",
                    models.CharField(
                        choices=[("✔", "OK"), ("✘", "Not OK")],
                        max_length=6,
                        verbose_name="Check Point 27",
                    ),
                ),
                (
                    "checkpoint_28",
                    models.CharField(
                        choices=[("✔", "OK"), ("✘", "Not OK")],
                        max_length=6,
                        verbose_name="Check Point 28",
                    ),
                ),
                (
                    "checkpoint_29",
                    models.CharField(
                        choices=[("✔", "OK"), ("✘", "Not OK")],
                        max_length=6,
                        verbose_name="Check Point 29",
                    ),
                ),
                (
                    "checkpoint_30",
                    models.CharField(
                        choices=[("✔", "OK"), ("✘", "Not OK")],
                        max_length=6,
                        verbose_name="Check Point 30",
                    ),
                ),
            ],
        ),
    ]
