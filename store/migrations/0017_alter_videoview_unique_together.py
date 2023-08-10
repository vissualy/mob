# Generated by Django 4.2.3 on 2023-08-10 21:43

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("store", "0016_videoview"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="videoview",
            unique_together={("user", "product")},
        ),
    ]
