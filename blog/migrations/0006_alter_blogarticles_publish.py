# Generated by Django 4.1 on 2024-07-01 14:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0005_alter_blogarticles_publish"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blogarticles",
            name="publish",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 7, 1, 14, 32, 4, 912992, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]