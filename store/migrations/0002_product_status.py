# Generated by Django 4.2.3 on 2023-08-02 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="status",
            field=models.CharField(
                choices=[("active", "active"), ("deleted", "deleted")],
                default="active",
                max_length=50,
            ),
        ),
    ]
