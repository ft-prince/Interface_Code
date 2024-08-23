# Generated by Django 5.1 on 2024-08-23 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("screen_app", "0063_alter_dailychecklistitem_machine_location_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dailychecklistitem",
            name="machine_name",
            field=models.CharField(
                choices=[
                    ("tsc_01", "TSC 01"),
                    ("tsc_02", "TSC 02"),
                    ("tsc_04", "TSC 04"),
                    ("tsc_05", "TSC 05"),
                    ("tsc_09", "TSC 09"),
                    ("ebe_01", "EBE 01"),
                    ("csl_01", "CSL 01"),
                    ("dtr_03", "DTR 03"),
                    ("dtr_05", "DTR 05"),
                ],
                max_length=100,
            ),
        ),
        migrations.AlterField(
            model_name="monthlychecklistitem",
            name="machine_name",
            field=models.CharField(
                choices=[
                    ("tsc_01", "TSC 01"),
                    ("tsc_02", "TSC 02"),
                    ("tsc_04", "TSC 04"),
                    ("tsc_05", "TSC 05"),
                    ("tsc_09", "TSC 09"),
                    ("ebe_01", "EBE 01"),
                    ("csl_01", "CSL 01"),
                    ("dtr_03", "DTR 03"),
                    ("dtr_05", "DTR 05"),
                ],
                max_length=100,
            ),
        ),
        migrations.AlterField(
            model_name="weeklychecklistitem",
            name="machine_name",
            field=models.CharField(
                choices=[
                    ("tsc_01", "TSC 01"),
                    ("tsc_02", "TSC 02"),
                    ("tsc_04", "TSC 04"),
                    ("tsc_05", "TSC 05"),
                    ("tsc_09", "TSC 09"),
                    ("ebe_01", "EBE 01"),
                    ("csl_01", "CSL 01"),
                    ("dtr_03", "DTR 03"),
                    ("dtr_05", "DTR 05"),
                ],
                max_length=100,
            ),
        ),
    ]
