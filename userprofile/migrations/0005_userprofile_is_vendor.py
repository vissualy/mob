# Generated by Django 4.2.3 on 2023-08-01 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("userprofile", "0004_vendor_image_alter_vendor_identification_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="userprofile",
            name="is_vendor",
            field=models.BooleanField(default=False),
        ),
    ]
