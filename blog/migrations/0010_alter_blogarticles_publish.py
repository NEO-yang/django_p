# Generated by Django 4.1 on 2024-07-09 09:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0009_alter_blogarticles_publish"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blogarticles",
            name="publish",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 7, 9, 9, 4, 9, 491842, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
