from django.utils.translation import gettext_lazy as _

from wagtail.models import Page
from wagtail.fields import StreamField
#from wagtail.admin.panels import StreamFieldPanel
from wagtail.admin.panels import FieldPanel

from wagtail.blocks import RichTextBlock
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
        #StreamFieldPanel('body', classname="full"),
        FieldPanel('body', classname="full"),
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