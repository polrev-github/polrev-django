import datetime
from django.utils import timezone
import us

from django.db import models
from django.utils.translation import ugettext_lazy as _

from modelcluster.fields import ParentalManyToManyField
from wagtail.core.models import Page
from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.core.fields import StreamField
from wagtail.search import index
from wagtail.admin.edit_handlers import StreamFieldPanel, RichTextField
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel, PageChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtailautocomplete.edit_handlers import AutocompletePanel

from wagtail.core.blocks import RichTextBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.embeds.blocks import EmbedBlock
from wagtailmarkdown.blocks import MarkdownBlock

from puput.utils import get_image_model_path

import us

class ElectionPage(Page):

    STATE_CHOICES = [(k, v) for k, v in us.states.mapping('fips', 'name').items()]

    state_fips = models.CharField(
        choices=STATE_CHOICES,
        verbose_name=_('State FIPS'),
        max_length=2,
        help_text=_("Example: 01, 02 ... 50"),
        default = '00'
    )

    date = models.DateTimeField(verbose_name=_("Election date"), default=timezone.now)

    body = StreamField([
        ('paragraph', RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('markdown', MarkdownBlock(icon="code")),
        ('embed', EmbedBlock(max_width=800, max_height=400))
    ], blank=True)
    
    excerpt = RichTextField(
        verbose_name=_('excerpt'),
        blank=True,
        help_text=_("Entry excerpt to be displayed on entries list. "
                    "If this field is not filled, a truncated version of body text will be used.")
    )

    image = models.ForeignKey(
        get_image_model_path(),
        verbose_name=_('Image'),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        ImageChooserPanel('image'),
        StreamFieldPanel('body', classname="full"),
        FieldPanel('excerpt'),
    ]

    parent_page_types = ['elections.YearPage']

    '''
    search_fields = Page.search_fields + [
    ]
    '''

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['election'] = self

        return context

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
