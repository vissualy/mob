# Generated by Django 4.2.3 on 2023-08-02 22:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("userprofile", "0011_alter_follow_user_alter_follow_vendor"),
    ]

    operations = [
        migrations.AddField(
            model_name="vendor",
            name="followers",
            field=models.ManyToManyField(
                related_name="follower_users",
                through="userprofile.Follow",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="follow",
            name="vendor",
            field=models.ForeignKey(
                blank=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="follower",
                to="userprofile.vendor",
            ),
        ),
    ]
