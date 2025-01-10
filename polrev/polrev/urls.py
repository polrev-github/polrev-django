from django.conf import settings
from django.urls import include, path, re_path
from django.contrib import admin
from django.views.generic.base import TemplateView

from wagtail.admin import urls as wagtailadmin_urls
from wagtail import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls
from wagtail.contrib.sitemaps.views import sitemap
from wagtailautocomplete.urls.admin import urlpatterns as autocomplete_admin_urls
from puput import urls as puput_urls

from search import views as search_views

#TODO:
from . import monkey_patch

urlpatterns = [
    re_path(r'^admin/autocomplete/', include(autocomplete_admin_urls)),

    path('django-admin/', admin.site.urls),

    path('admin/', include(wagtailadmin_urls)),
    path('documents/', include(wagtaildocs_urls)),

    #path('search/', search_views.search, name='search'),
    path('sitemap.xml', sitemap),
    path("robots.txt",TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
]

urlpatterns = urlpatterns + [
    path('', include('home.urls')),

    path('accounts/', include('allauth.urls')),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),

    path('join-the-revolution-on-slack/', include('slack_invite.urls')),

    # Portals
    path('run/', include('portals.run.urls')),
    path('volunteer/', include('portals.volunteer.urls')),

    re_path(r'^comments/', include('django_comments_xtd.urls')),
    re_path(r'^tz_detect/', include('tz_detect.urls')),
    path("", include(puput_urls)),
    path("", include(wagtail_urls)),

]