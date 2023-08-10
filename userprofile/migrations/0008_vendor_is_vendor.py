# Generated by Django 4.2.3 on 2023-08-01 20:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("userprofile", "0007_alter_vendor_status"),
    ]

    operations = [
        migrations.AddField(
            model_name="vendor",
            name="is_vendor",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="userprofile.userprofile",
            ),
        ),
    ]