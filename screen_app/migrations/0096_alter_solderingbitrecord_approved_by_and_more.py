# Generated by Django 5.1 on 2024-09-08 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("screen_app", "0095_startupchecksheet_manager_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="solderingbitrecord",
            name="approved_by",
            field=models.CharField(
                blank=True, choices=[("20d", "20D"), ("30d", "30D")], max_length=100
            ),
        ),
        migrations.AlterField(
            model_name="solderingbitrecord",
            name="bit_size",
            field=models.CharField(
                choices=[("20d", "20D"), ("30d", "30D")], max_length=50
            ),
        ),
        migrations.AlterField(
            model_name="solderingbitrecord",
            name="prepared_by",
            field=models.CharField(
                blank=True, choices=[("20d", "20D"), ("30d", "30D")], max_length=100
            ),
        ),
    ]
