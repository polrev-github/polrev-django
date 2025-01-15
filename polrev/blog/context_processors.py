from puput.models import BlogPage
from puput.models import EntryPage

def blog(request):
    return {
        'blog_page': BlogPage.objects.first(),
        'featured_articles': EntryPage.objects.live().filter(featured=True)
    }

'''
def header_image(request):
    return {'header_image': 'img/site-header-cropped.jpg'}
'''

'''
def header_image(request):
    return {'header_image': 'img/site-header-tall.jpg'}
'''

def header_image(request):
    if request.path != '/' and request.user_agent.is_pc:  # Home page
        return {'header_image': 'img/site-header.jpg'}
    else:  # Other pages
        return {'header_image': 'img/site-header-tall.jpg'}

'''
def header_image(request):
    if request.path == '/':  # Home page
        return {'header_image': 'img/site-header-tall.jpg'}
    else:  # Other pages
        return {'header_image': 'img/site-header.jpg'}
'''