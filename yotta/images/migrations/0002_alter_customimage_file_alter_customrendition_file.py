# Generated by Django 5.0.4 on 2024-05-01 12:24

import wagtail.images.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("images", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customimage",
            name="file",
            field=wagtail.images.models.WagtailImageField(
                height_field="height",
                upload_to=wagtail.images.models.get_upload_to,
                verbose_name="file",
                width_field="width",
            ),
        ),
        migrations.AlterField(
            model_name="customrendition",
            name="file",
            field=wagtail.images.models.WagtailImageField(
                height_field="height",
                storage=wagtail.images.models.get_rendition_storage,
                upload_to=wagtail.images.models.get_rendition_upload_to,
                width_field="width",
            ),
        ),
    ]