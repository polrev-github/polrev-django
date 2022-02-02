from django.utils.translation import ugettext_lazy as _

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import StreamFieldPanel

from wagtail.core.blocks import RichTextBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.embeds.blocks import EmbedBlock
from wagtailmarkdown.blocks import MarkdownBlock

#from puput.models import BlogPage
#from puput.models import EntryPage

class HomePage(Page):
    body = StreamField([
        ('paragraph', RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('markdown', MarkdownBlock(icon="code")),
        ('embed', EmbedBlock(max_width=800, max_height=400))
    ], blank=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel('body', classname="full"),
    ]
    '''
    def get_context(self, request, *args, **kwargs):
        context = super().get_context(
            request, *args, **kwargs)
        context['blog_page'] = BlogPage.objects.first()
        featured_articles = EntryPage.objects.live().filter(featured=True)
        context['featured_articles'] = featured_articles
        return context
    '''