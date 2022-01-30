from puput.models import BlogPage
from puput.models import EntryPage

def blog(request):
    return {
        'blog_page': BlogPage.objects.first(),
        'featured_articles': EntryPage.objects.live().filter(featured=True)
    }