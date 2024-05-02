from modelcluster.models import ClusterableModel
from wagtail.models import StreamField
from yotta.navigation.blocks import (
    LinkBlock,
    PrimaryNavLinkBlock,
)
from wagtail.admin.panels import FieldPanel
from wagtail.contrib.settings.models import BaseSiteSetting, register_setting


@register_setting(icon="list-ul")
class NavigationSettings(BaseSiteSetting, ClusterableModel):
    primary_navigation = StreamField(
        [("link", PrimaryNavLinkBlock())],
        blank=True,
        help_text="Main site navigation",
    )
    footer_links = StreamField(
        [("link", LinkBlock())],
        blank=True,
        help_text="Single list of elements at the base of the page.",
    )

    panels = [
        FieldPanel("primary_navigation"),
        FieldPanel("footer_links"),
    ]
