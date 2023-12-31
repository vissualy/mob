# Generated by Django 4.2.3 on 2023-08-02 20:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("userprofile", "0009_remove_vendor_is_vendor"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="mobile_number",
            field=models.IntegerField(null=True),
        ),
        migrations.CreateModel(
            name="Follow",
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
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="following",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "vendor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="followers",
                        to="userprofile.vendor",
                    ),
                ),
            ],
            options={
                "unique_together": {("user", "vendor")},
            },
        ),
    ]
