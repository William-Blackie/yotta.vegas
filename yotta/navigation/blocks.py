from django.core.exceptions import ValidationError
from django.forms.utils import ErrorList

from wagtail import blocks
from wagtail.blocks.struct_block import StructBlockValidationError


class LinkBlockStructValue(blocks.StructValue):
    def url(self):
        if page := self.get("page"):
            return page.url

        if external_link := self.get("external_link"):
            return external_link

        return ""

    def text(self):
        if self.get("page") and not self.get("title"):
            return self.get("page").title
        if title := self.get("title"):
            return title
        return ""

    def is_page(self):
        return bool(self.get("page"))


class LinkValidationMixin:
    """
    Ensures that you cannot select both an external and an internal link.
    Used by both LinkBlock FooterLinkBlock
    """

    def clean(self, value):
        struct_value = super().clean(value)

        errors = {}
        page = value.get("page")
        external_link = value.get("external_link")

        if not page and not external_link:
            error = ErrorList(
                [ValidationError("You must specify either a page or an external link")]
            )
            errors["page"] = errors["external_link"] = error

        if page and external_link:
            error = ErrorList(
                [
                    ValidationError(
                        "You must specify either a page or an external link, not both"
                    )
                ]
            )
            errors["external_link"] = errors["page"] = error

        if errors:
            raise StructBlockValidationError(errors)
        return struct_value


class LinkBlock(LinkValidationMixin, blocks.StructBlock):
    """
    Used to select links for the primary navigation and for the footer links
    """

    page = blocks.PageChooserBlock(required=False)
    external_link = blocks.URLBlock(required=False)
    title = blocks.CharBlock(
        help_text="Leave blank to use the page's own title",
        required=False,
        label="Navigation text",
    )

    class Meta:
        value_class = LinkBlockStructValue

    def clean(self, value):
        """
        Additional validation to ensure that a link title is specified for external links
        """
        struct_value = super().clean(value)

        errors = {}
        external_link = value.get("external_link")

        if not value.get("title") and external_link:
            error = ErrorList(
                [ValidationError("You must specify the link title for external links")]
            )
            errors["title"] = error

        if errors:
            raise StructBlockValidationError(errors)
        return struct_value


class FooterLinkBlock(LinkValidationMixin, blocks.StructBlock):
    """
    Used to select links for the footer logos
    """

    page = blocks.PageChooserBlock(required=False)
    external_link = blocks.URLBlock(required=False)

    class Meta:
        value_class = LinkBlockStructValue


class PrimaryNavLinkBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True)
    page = blocks.PageChooserBlock(required=False)
    external_link = blocks.URLBlock(required=False)

    children = blocks.ListBlock(
        LinkBlock()
    )

    def clean(self, value):
        struct_value = super().clean(value)

        errors = {}
        link = value.get("page") or value.get("external_link")
        children = value.get("children")

        if link and children:
            error = ErrorList(
                [ValidationError("You must specify either child links or a main link, not both")]
            )
            errors["page"] = errors["external_link"] = errors["children"] = error

        if not link and not children:
            error = ErrorList(
                [
                    ValidationError(
                        "You must specify either a main link or child links"
                    )
                ]
            )
            errors["page"] = errors["external_link"] = errors["children"] = error

        if errors:
            raise StructBlockValidationError(errors)
        return struct_value

