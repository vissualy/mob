# Generated by Django 4.2.3 on 2023-08-01 20:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("userprofile", "0008_vendor_is_vendor"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="vendor",
            name="is_vendor",
        ),
    ]