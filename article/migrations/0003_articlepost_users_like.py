# Generated by Django 4.1 on 2024-07-08 07:35

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("article", "0002_articlepost"),
    ]

    operations = [
        migrations.AddField(
            model_name="articlepost",
            name="users_like",
            field=models.ManyToManyField(
                blank=True, related_name="articles_like", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
