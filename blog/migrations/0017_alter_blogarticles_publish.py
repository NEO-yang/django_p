# Generated by Django 4.1 on 2024-07-10 14:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0016_alter_blogarticles_publish"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blogarticles",
            name="publish",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 7, 10, 14, 45, 12, 710971, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
