# Generated by Django 4.2.3 on 2023-08-06 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0012_imagemodel_remove_product_image_product_image"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="image",
        ),
        migrations.DeleteModel(
            name="Imagemodel",
        ),
        migrations.AddField(
            model_name="product",
            name="image",
            field=models.ImageField(blank=True, upload_to="images/productimage"),
        ),
    ]