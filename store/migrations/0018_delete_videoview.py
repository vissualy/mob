# Generated by Django 4.2.3 on 2023-08-10 21:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0017_alter_videoview_unique_together"),
    ]

    operations = [
        migrations.DeleteModel(
            name="VideoView",
        ),
    ]
