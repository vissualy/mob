# Generated by Django 4.2.3 on 2023-08-04 01:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("userprofile", "0014_vendor_followers"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="vendor",
            name="followers",
        ),
        migrations.DeleteModel(
            name="Follow",
        ),
    ]
