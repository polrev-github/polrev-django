from django.db import models

from django.utils.translation import ugettext_lazy as _

from wagtail.core.models import Page
from wagtail.core.fields import StreamField

from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel, PageChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel

from wagtail.core.blocks import RichTextBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.embeds.blocks import EmbedBlock
from wagtailmarkdown.blocks import MarkdownBlock

from puput.utils import get_image_model_path

class StatesPage(Page):
    body = StreamField([
        ('paragraph', RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('markdown', MarkdownBlock(icon="code")),
        ('embed', EmbedBlock(max_width=800, max_height=400))
    ], blank=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel('body', classname="full"),
    ]

    # Parent page / subpage type rules
    parent_page_types = ['home.HomePage']
    subpage_types = ['states.StatePage']

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(
            request, *args, **kwargs)
        context['states'] = StatePage.objects.all()
        return context


class StatePage(Page):
    subtitle = models.CharField(
        verbose_name=_('subtitle'),
        max_length=255,
        help_text=_("Example: Ua Mau ke Ea o ka ‘Āina i ka Pono")
    )

    abbreviation = models.CharField(
        verbose_name=_('abbreviation'),
        max_length=2,
        help_text=_("Example: AK, AL, AR")
    )

    body = StreamField([
        ('paragraph', RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('markdown', MarkdownBlock(icon="code")),
        ('embed', EmbedBlock(max_width=800, max_height=400))
    ], blank=True)

    header_image = models.ForeignKey(
        get_image_model_path(),
        verbose_name=_('Header image'),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel('subtitle', classname="subtitle"),
        FieldPanel('abbreviation', classname="abbreviation"),
        ImageChooserPanel('header_image'),
        StreamFieldPanel('body', classname="full"),
    ]

    # Parent page / subpage type rules
    parent_page_types = ['states.StatesPage']
    subpage_types = []