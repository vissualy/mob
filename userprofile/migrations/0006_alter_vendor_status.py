# Generated by Django 4.2.3 on 2023-08-01 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("userprofile", "0005_userprofile_is_vendor"),
    ]

    operations = [
        migrations.AlterField(
            model_name="vendor",
            name="status",
            field=models.CharField(
                choices=[
                    ("submitted", "submitted"),
                    ("declined", "declined"),
                    ("accepted", "accepted"),
                ],
                default="submitted",
                max_length=100,
            ),
        ),
    ]