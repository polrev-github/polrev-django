from django.utils.translation import gettext_lazy as _

from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel

from wagtail.blocks import RichTextBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.embeds.blocks import EmbedBlock
from wagtailmarkdown.blocks import MarkdownBlock


class InfoPage(Page):
    body = StreamField(
        [
            ("paragraph", RichTextBlock()),
            ("image", ImageChooserBlock()),
            ("markdown", MarkdownBlock(icon="code")),
            ("embed", EmbedBlock(max_width=800, max_height=400)),
        ],
        blank=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("body", classname="full"),
    ]

    parent_page_types = ["home.HomePage"]
