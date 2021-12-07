from django.core.management.base import BaseCommand
#from wagtail.core.models import Site
from django.contrib.sites.models import Site
from django.conf import settings

from accounts.models import User
from blog.models import Post

class Command(BaseCommand):
    help = 'Populate Database'

    def handle(self, *args, **kwargs):
        site = Site.objects.get(pk=settings.SITE_ID)
        site.domain = settings.HOSTNAME
        site.name = settings.WAGTAIL_SITE_NAME
        site.save()

        user = User.objects.create_user(username='john',
            first_name='John',
            last_name='Doe',
            email='john@nowhere.com',
            password='password')
        post = Post.objects.create(owner=user,
            title="I love Python",
            body="What a great language!",
            path='i-love-python',
            depth=1,
             )
        user = User.objects.create_user(username='susan',
            first_name='Susan',
            last_name='Smith',
            email='susan@nowhere.com',
            password='password')
        post = Post.objects.create(owner=user,
            title="I love Django",
            body="What a great framework!",
            path='i-love-django',
            depth=1,
             )
