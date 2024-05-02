# Generated by Django 5.0.4 on 2024-05-01 12:45

import wagtail.blocks
import wagtail.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("navigation", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="navigationsettings",
            name="primary_navigation",
            field=wagtail.fields.StreamField(
                [
                    (
                        "link",
                        wagtail.blocks.StructBlock(
                            [
                                ("title", wagtail.blocks.CharBlock(required=True)),
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
    ]
