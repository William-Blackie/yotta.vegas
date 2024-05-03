from wagtail import blocks
from django.forms.utils import ErrorList
from wagtail.fields import StreamField
from wagtail.images.blocks import ImageChooserBlock
from wagtail.documents.blocks import DocumentChooserBlock
from os import listdir
from os.path import isfile, join
from django.core.exceptions import ValidationError
from wagtail.blocks import StructValue
from yotta.utils.constants import TAILWIND_COLOR_CHOICES

class LinkStructValue(StructValue):
    def url(self):
        external_url = self.get('external_link')
        internal_link = self.get('internal_link')
        return external_url or internal_link.url

class InternalExternalLinkBlock(blocks.StructBlock):
    """
    A block that allows you to choose between an internal or external link.
    """
    internal_link = blocks.PageChooserBlock(required=False)
    external_link = blocks.URLBlock(required=False)

    class Meta:
        icon = 'link'
        template = 'utils/blocks/internal_external_link.html'

    def clean(self, value):
        errors = {}
        if value.get('internal_link') and value.get('external_link'):
            msg =  'Only one of these fields should be filled out.'
            errors['internal_link'] = ErrorList([
                msg
            ])
            errors['external_link'] = ErrorList([
                msg
            ])

        if not value.get('internal_link') and not value.get('external_link'):
            msg = 'You must fill out one of these fields.'
            errors['internal_link'] = ErrorList([
                msg
            ])
            errors['external_link'] = ErrorList([
                msg
            ])

        if errors:
            raise ValidationError('Validation error in InternalExternalLinkBlock', params=errors)

        return super(InternalExternalLinkBlock, self).clean(value)

    class Meta:
        value_class = LinkStructValue


class CardBlock(blocks.StructBlock):
    """
    A card block with an image, title, and link.
    """
    title = blocks.CharBlock(required=True)
    text = blocks.RichTextBlock(required=True)
    link = InternalExternalLinkBlock(required=True)
    image = ImageChooserBlock(required=False)

    class Meta:
        icon = 'placeholder'
        template = 'components/blocks/cards/card_block.html'

class CardsBlock(blocks.StructBlock):
    """
    A block that contains a list of cards.
    """
    card = blocks.ListBlock(CardBlock())

    class Meta:
        icon = 'placeholder'
        template = 'components/blocks/cards/cards_block.html'

class ImageWithCaptionBlock(ImageChooserBlock):
    """
    A ImageChooserBlock with caption and alt text.
    """
    caption = blocks.CharBlock(required=False)
    alt_text = blocks.CharBlock(required=True)

    class Meta:
        icon = 'image'

class CodeBlock(blocks.StructBlock):
    """
    A block for code snippets.
    """
    code = blocks.TextBlock(required=True)
    language = blocks.CharBlock(required=False)

    class Meta:
        icon = 'code'
        template = 'components/blocks/code_block.html'

class ImageTextBlock(blocks.StructBlock):
    """
    A block for an image with text.
    """
    image = ImageWithCaptionBlock(required=True)
    text = blocks.RichTextBlock(required=True)

    class Meta:
        icon = 'placeholder'
        template = 'components/blocks/image_text_block.html'


class TailwindColorStructValue(StructValue):
    def text_color(self):
        return "text-" + self.get('color')
    
    def background_color(self):
        return "bg-" + self.get('color')

class ColorBlock(blocks.StructBlock):
    """
    A block for a color.
    """
    color = blocks.ChoiceBlock(
        choices=TAILWIND_COLOR_CHOICES,
    )

    class Meta:
        value_class = TailwindColorStructValue

class IntroWithTextGridBlock(blocks.StructBlock):
    """
    A block for an intro with text grid.
    """
    title_start = blocks.CharBlock(required=True)
    title_middle = blocks.CharBlock(required=True)
    title_end = blocks.CharBlock(required=True)
    intro = blocks.RichTextBlock(required=True)
    text_grid = blocks.ListBlock(
        blocks.StructBlock([
            ('heading', blocks.CharBlock(required=True)),
            ('text', blocks.RichTextBlock(required=True)),
        ])
    )
    class Meta:
        icon = 'placeholder'
        template = 'components/blocks/intro_with_text_grid.html'


class LogoBlock(blocks.StructBlock):
    """
    A block for a list of logos.
    """
    title = blocks.CharBlock(required=True)
    logos = blocks.ListBlock(
        blocks.StructBlock([
            ('logo', ImageChooserBlock(required=True)),
        ])
    )
    class Meta:
        icon = 'placeholder'
        template = 'components/blocks/logo_block.html'


class PeopleBlock(blocks.StructBlock):
    """
    A block for a list of people.
    """
    title = blocks.CharBlock(required=True)
    intro = blocks.CharBlock(required=True)
    people = blocks.ListBlock(
        blocks.StructBlock([
            ('name', blocks.CharBlock(required=True)),
            ('role', blocks.CharBlock(required=True)),
            ('company', blocks.CharBlock(required=True)),
            ('image', ImageChooserBlock(required=True)),
        ])
    )
    class Meta:
        icon = 'placeholder'
        template = 'components/blocks/people_block.html'

class ContentStreamField(blocks.StreamBlock):
    """"
    A StreamField that contains all the blocks that can be used in the general content.
    """
    heading = blocks.CharBlock(
        template='components/blocks/heading_block.html',
    )
    paragraph = blocks.RichTextBlock(
        template="components/blocks/paragraph_block.html"
    )
    intro_with_text_grid = IntroWithTextGridBlock()
    document = DocumentChooserBlock()
    image_text = ImageTextBlock()
    people_block = PeopleBlock()    
    logo_block = LogoBlock()
    
    class Meta:
        template = 'components/blocks/content.html'

