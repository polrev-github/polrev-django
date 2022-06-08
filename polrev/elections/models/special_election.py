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


from .election import ElectionPage

class SpecialElectionPage(ElectionPage):

    area_ref = models.ForeignKey(
        'areas.Area',
        on_delete=models.PROTECT,
        related_name='elections',
    )

    office_type_ref = models.ForeignKey(
        'offices.OfficeType',
        verbose_name=_('office type'),
        on_delete=models.PROTECT,
        related_name='elections',
    )

    office_ref = models.ForeignKey(
        'offices.Office',
        on_delete=models.PROTECT,
        related_name='elections',
    )

    office_panels = []

    content_panels = ElectionPage.content_panels + [
    ]

    parent_page_types = ['elections.YearPage']
