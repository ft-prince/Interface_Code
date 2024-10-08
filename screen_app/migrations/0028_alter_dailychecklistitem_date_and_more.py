# Generated by Django 5.0.6 on 2024-08-15 06:24

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("screen_app", "0027_alter_dailychecklistitem_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dailychecklistitem",
            name="date",
            field=models.DateField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name="dailychecklistitem",
            name="month_year",
            field=models.DateField(blank=True, default=django.utils.timezone.now),
        ),
    ]
