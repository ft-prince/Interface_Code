# Generated by Django 5.1 on 2024-08-24 08:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("screen_app", "0069_remove_startupchecksheet_checkpoint_26_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="startupchecksheet",
            options={
                "verbose_name": "Start Up Check Sheet",
                "verbose_name_plural": "Start Up Check Sheets",
            },
        ),
    ]
