import datetime

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import truncatechars
from django.utils.text import Truncator
from django.utils.safestring import mark_safe
from django.utils.html import strip_tags

from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.admin.edit_handlers import (
    FieldPanel,
    MultiFieldPanel,
    InlinePanel,
    PageChooserPanel,
)
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.fields import RichTextField
from modelcluster.contrib.taggit import ClusterTaggableManager

from wagtail.core.blocks import StreamBlock, RichTextBlock, TextBlock, CharBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.embeds.blocks import EmbedBlock
from wagtailmarkdown.blocks import MarkdownBlock

from puput.utils import get_image_model_path


class EntryAbstract(models.Model):
    body = StreamField(
        [
            ("paragraph", RichTextBlock()),
            ("image", ImageChooserBlock()),
            ("markdown", MarkdownBlock(icon="code")),
            ("embed", EmbedBlock(max_width=800, max_height=400)),
        ]
    )
    tags = ClusterTaggableManager(through="puput.TagEntryPage", blank=True)
    date = models.DateTimeField(
        verbose_name=_("Post date"), default=datetime.datetime.today
    )
    header_image = models.ForeignKey(
        get_image_model_path(),
        verbose_name=_("Header image"),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    categories = models.ManyToManyField(
        "puput.Category", through="puput.CategoryEntryPage", blank=True
    )
    excerpt = RichTextField(
        verbose_name=_("excerpt"),
        blank=True,
        help_text=_(
            "Entry excerpt to be displayed on entries list. "
            "If this field is not filled, a truncated version of body text will be used."
        ),
    )
    num_comments = models.IntegerField(default=0, editable=False)
    featured = models.BooleanField(default=False)

    content_panels = [
        MultiFieldPanel(
            [
                FieldPanel("title", classname="title"),
                FieldPanel("featured"),
                ImageChooserPanel("header_image"),
                StreamFieldPanel("body", classname="full"),
                FieldPanel("excerpt", classname="full"),
            ],
            heading=_("Content"),
        ),
        MultiFieldPanel(
            [
                FieldPanel("tags"),
                InlinePanel("entry_categories", label=_("Categories")),
                InlinePanel(
                    "related_entrypage_from",
                    label=_("Related Entries"),
                    panels=[PageChooserPanel("entrypage_to")],
                ),
            ],
            heading=_("Metadata"),
        ),
    ]

    class Meta:
        abstract = True

    def get_excerpt(self, length=300):
        if self.excerpt:
            # Use the manually provided excerpt
            return mark_safe(self.excerpt)
        else:
            # Extract text content from the StreamField
            text_content = strip_tags(
                "".join(
                    block.render(block)
                    for block in self.body
                    if block.block_type == "paragraph"
                )
            )

            # Truncate the text content to the specified length
            truncated_content = Truncator(text_content).chars(length, truncate="…")
            return mark_safe(truncated_content)

    """
    def get_excerpt(self, length=300):
        if self.excerpt:
            # Use the manually provided excerpt
            return self.excerpt
        else:
            # Extract text content from the StreamField
            text_content = ''.join(
                block.render_as_block(block) for block in self.body if block.block_type == 'paragraph'
            )

            # Truncate the text content to the specified length
            return Truncator(text_content).chars(length, truncate='…')
    """

    """
    def get_excerpt(self, length=100):
        # Extract text content from the StreamField
        text_content = ''.join(
            block.render_as_block(block.value) for block in self.body if isinstance(block, RichTextBlock)
        )

        # Truncate the text content to the specified length
        return Truncator(text_content).chars(length, truncate='…')
    """

    """
    def get_excerpt(self, length=100):
        if self.excerpt:
            # Use the manually provided excerpt
            return self.excerpt
        else:
            # Extract text content from the StreamField
            text_content = ''.join(
                block.render_as_block(block.value) for block in self.body if isinstance(block, RichTextBlock)
            )

            # Truncate the text content to the specified length
            return Truncator(text_content).chars(length, truncate='…')
    """
