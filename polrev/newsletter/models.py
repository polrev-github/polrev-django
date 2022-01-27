from django.db import models

from birdsong.blocks import DefaultBlocks
from birdsong.models import Campaign

from wagtail.admin.edit_handlers import StreamFieldPanel, FieldPanel, TabbedInterface, ObjectList
from wagtail.core.fields import StreamField
from wagtail.images.edit_handlers import ImageChooserPanel

from birdsong.models import Contact

from .panels import PreviewPanel

'''
class ExtendedContact(Contact):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
'''

class Newsletter(Campaign):
    headline = models.CharField(
        max_length=255,
        help_text="The headline to use for the newsletter."
    )

    header_background = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        related_name="+",
        help_text="The image to use for the header backgound.",
        on_delete=models.SET_NULL,
    )

    body = StreamField(DefaultBlocks())

    content_panels = Campaign.panels + [
        FieldPanel("headline"),
        ImageChooserPanel("header_background"),
        StreamFieldPanel("body"),
    ]

    preview_panels = [
        PreviewPanel('preview'),
    ]
    edit_handler = TabbedInterface([
        ObjectList(content_panels, heading='Content'),
        ObjectList(preview_panels, heading='Preview'),
    ])