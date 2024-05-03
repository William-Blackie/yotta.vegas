from django.db import models

from yotta.utils.models import BasePage
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField
from yotta.utils.blocks import ContentStreamField


class HomePage(BasePage):
    template = 'pages/home_page.html'

    title_start = models.CharField(max_length=50, blank=False, default="How will digital infrastructure meet")
    title_end = models.CharField(max_length=50, blank=False, default="the demands of AI?")
    intro = models.TextField(default="Join us in Las Vegas on October 7-9 for an epic large-scale show exploring where this trillion dollar industry goes next...")

    body = StreamField(
        ContentStreamField(),
        null=True, blank=True, use_json_field=True
    )

    content_panels = BasePage.content_panels + [
        # Hero
        FieldPanel("title_start"),
        FieldPanel("title_end"),
        FieldPanel("intro"),
        # Content
        FieldPanel("body"),
    ]
