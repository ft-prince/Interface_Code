# Generated by Django 5.1 on 2024-08-23 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("screen_app", "0061_alter_monthlychecklistitem_doc_number"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="weeklychecklistitem",
            options={},
        ),
        migrations.AlterField(
            model_name="dailychecklistitem",
            name="control_number",
            field=models.CharField(
                choices=[
                    ("51-00-4283-3", "51-00-4283-3"),
                    ("51-00-2603-3", "51-00-2603-3"),
                    ("51-00-1466-3", "51-00-1466-3"),
                    ("57-00-2141-3", "57-00-2141-3"),
                    ("57-00-1891-3", "57-00-1891-3"),
                    ("56-00-1702-3", "56-00-1702-3"),
                    ("56-00-2461-2", "56-00-2461-2"),
                    ("56-00-1019-2", "56-00-1019-2"),
                    ("56-00-1454-2", "56-00-1454-2"),
                    ("56-00-1737-3", "56-00-1737-3"),
                    ("56-00-2305-3", "56-00-2305-3"),
                    ("51-00-2305-3", "51-00-2305-3"),
                    ("51-00-3585-3", "51-00-3585-3"),
                    ("51-00-2629-3", "51-00-2629-3"),
                    ("57-00-1578-3", "57-00-1578-3"),
                    ("57-00-1579-3", "57-00-1579-3"),
                    ("51-00-3228-3", "51-00-3228-3"),
                    ("56-00-2450-3", "56-00-2450-3"),
                    ("52-00-1035-1", "52-00-1035-1"),
                ],
                max_length=100,
            ),
        ),
        migrations.AlterField(
            model_name="monthlychecklistitem",
            name="control_number",
            field=models.CharField(
                choices=[
                    ("51-00-4283-3", "51-00-4283-3"),
                    ("51-00-2603-3", "51-00-2603-3"),
                    ("51-00-1466-3", "51-00-1466-3"),
                    ("57-00-2141-3", "57-00-2141-3"),
                    ("57-00-1891-3", "57-00-1891-3"),
                    ("56-00-1702-3", "56-00-1702-3"),
                    ("56-00-2461-2", "56-00-2461-2"),
                    ("56-00-1019-2", "56-00-1019-2"),
                    ("56-00-1454-2", "56-00-1454-2"),
                    ("56-00-1737-3", "56-00-1737-3"),
                    ("56-00-2305-3", "56-00-2305-3"),
                    ("51-00-2305-3", "51-00-2305-3"),
                    ("51-00-3585-3", "51-00-3585-3"),
                    ("51-00-2629-3", "51-00-2629-3"),
                    ("57-00-1578-3", "57-00-1578-3"),
                    ("57-00-1579-3", "57-00-1579-3"),
                    ("51-00-3228-3", "51-00-3228-3"),
                    ("56-00-2450-3", "56-00-2450-3"),
                    ("52-00-1035-1", "52-00-1035-1"),
                ],
                max_length=100,
            ),
        ),
        migrations.AlterField(
            model_name="weeklychecklistitem",
            name="control_number",
            field=models.CharField(
                choices=[
                    ("51-00-4283-3", "51-00-4283-3"),
                    ("51-00-2603-3", "51-00-2603-3"),
                    ("51-00-1466-3", "51-00-1466-3"),
                    ("57-00-2141-3", "57-00-2141-3"),
                    ("57-00-1891-3", "57-00-1891-3"),
                    ("56-00-1702-3", "56-00-1702-3"),
                    ("56-00-2461-2", "56-00-2461-2"),
                    ("56-00-1019-2", "56-00-1019-2"),
                    ("56-00-1454-2", "56-00-1454-2"),
                    ("56-00-1737-3", "56-00-1737-3"),
                    ("56-00-2305-3", "56-00-2305-3"),
                    ("51-00-2305-3", "51-00-2305-3"),
                    ("51-00-3585-3", "51-00-3585-3"),
                    ("51-00-2629-3", "51-00-2629-3"),
                    ("57-00-1578-3", "57-00-1578-3"),
                    ("57-00-1579-3", "57-00-1579-3"),
                    ("51-00-3228-3", "51-00-3228-3"),
                    ("56-00-2450-3", "56-00-2450-3"),
                    ("52-00-1035-1", "52-00-1035-1"),
                ],
                max_length=100,
            ),
        ),
    ]
