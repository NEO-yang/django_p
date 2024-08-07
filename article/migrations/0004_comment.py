# Generated by Django 4.1 on 2024-07-09 09:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("article", "0003_articlepost_users_like"),
    ]

    operations = [
        migrations.CreateModel(
            name="Comment",
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
                ("commentator", models.CharField(max_length=90)),
                ("body", models.TextField()),
                ("created", models.DateTimeField(auto_now_add=True)),
                (
                    "article",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comments",
                        to="article.articlepost",
                    ),
                ),
            ],
            options={"ordering": ("-created",),},
        ),
    ]
