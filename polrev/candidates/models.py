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

from wagtailautocomplete.edit_handlers import AutocompletePanel

from puput.utils import get_image_model_path

class CandidatesPage(Page):
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
    subpage_types = ['candidates.CandidatePage']

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(
            request, *args, **kwargs)
        #context['candidates'] = CandidatePage.objects.all()
        context['candidates'] = CandidatePage.objects.order_by('state__title')
        return context


class CandidatePage(Page):
    subtitle = models.CharField(
        verbose_name=_('subtitle'),
        max_length=255,
        help_text=_("Example: Candidate, U.S. Senate OH | Candidate, U.S. House OH-11")
    )

    state = models.ForeignKey(
        'states.StatePage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='candidates',
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

    featured = models.BooleanField(default=False)

    # Social Media
    facebook = models.URLField("facebook", blank=True)
    twitter = models.URLField("twitter", blank=True)
    instagram = models.URLField("instagram", blank=True)
    website = models.URLField("website", blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('subtitle', classname="subtitle"),
        #PageChooserPanel('state', 'states.StatePage'),
        AutocompletePanel('state'),
        FieldPanel('featured'),
        ImageChooserPanel('header_image'),
        StreamFieldPanel('body', classname="full"),
        FieldPanel('facebook'),
        FieldPanel('twitter'),
        FieldPanel('instagram'),
        FieldPanel('website'),
    ]

    # Parent page / subpage type rules
    parent_page_types = ['candidates.CandidatesPage']
    subpage_types = []