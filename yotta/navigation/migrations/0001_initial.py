# Generated by Django 5.0.4 on 2024-05-01 12:24

import django.db.models.deletion
import wagtail.blocks
import wagtail.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("wagtailcore", "0091_remove_revision_submitted_for_moderation"),
    ]

    operations = [
        migrations.CreateModel(
            name="NavigationSettings",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "primary_navigation",
                    wagtail.fields.StreamField(
                        [
                            (
                                "link",
                                wagtail.blocks.StructBlock(
                                    [
                                        (
                                            "title",
                                            wagtail.blocks.CharBlock(required=True),
                                        ),
                                        (
                                            "children",
                                            wagtail.blocks.ListBlock(
                                                wagtail.blocks.StructBlock(
                                                    [
                                                        (
                                                            "page",
                                                            wagtail.blocks.PageChooserBlock(
                                                                required=False
                                                            ),
                                                        ),
                                                        (
                                                            "external_link",
                                                            wagtail.blocks.URLBlock(
                                                                required=False
                                                            ),
                                                        ),
                                                        (
                                                            "title",
                                                            wagtail.blocks.CharBlock(
                                                                help_text="Leave blank to use the page's own title",
                                                                label="Navigation text",
                                                                required=False,
                                                            ),
                                                        ),
                                                    ]
                                                )
                                            ),
                                        ),
                                    ]
                                ),
                            )
                        ],
                        blank=True,
                        help_text="Main site navigation",
                    ),
                ),
                (
                    "footer_links",
                    wagtail.fields.StreamField(
                        [
                            (
                                "link",
                                wagtail.blocks.StructBlock(
                                    [
                                        (
                                            "page",
                                            wagtail.blocks.PageChooserBlock(
                                                required=False
                                            ),
                                        ),
                                        (
                                            "external_link",
                                            wagtail.blocks.URLBlock(required=False),
                                        ),
                                        (
                                            "title",
                                            wagtail.blocks.CharBlock(
                                                help_text="Leave blank to use the page's own title",
                                                label="Navigation text",
                                                required=False,
                                            ),
                                        ),
                                    ]
                                ),
                            )
                        ],
                        blank=True,
                        help_text="Single list of elements at the base of the page.",
                    ),
                ),
                (
                    "site",
                    models.OneToOneField(
                        editable=False,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="wagtailcore.site",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]