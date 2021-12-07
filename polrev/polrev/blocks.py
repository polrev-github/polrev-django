
from django.utils.safestring import mark_safe
from markdown import markdown
from pygments import highlight
from pygments.formatters import get_formatter_by_name
from pygments.lexers import get_lexer_by_name
from django.utils.safestring import mark_safe
from markdown import markdown
from wagtail.core.blocks import (
    StreamBlock, 
    RichTextBlock,
    TextBlock,
    CharBlock 
)
from wagtail.images.blocks import ImageChooserBlock
#from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.embeds.blocks import EmbedBlock
from wagtailcodeblock.blocks import CodeBlock
from wagtailmarkdown.blocks import MarkdownBlock


class ContentStreamBlock(StreamBlock):
    h2 = CharBlock(icon="title", classname="title")
    h3 = CharBlock(icon="title", classname="title")
    h4 = CharBlock(icon="title", classname="title")
    paragraph = RichTextBlock(required=False)
    image = ImageChooserBlock(required=False)
    code = CodeBlock(label='Code', required=False)
    embeds = EmbedBlock(required=False)
    markdown = MarkdownBlock(required=False)

    # class Meta:
    #     template = 'puput/code_block1.html'


