from puput.models import EntryPage

def get_sitemap_urls(self, request=None):
    from puput.urls import get_entry_url
    from wagtail.models import Site
    root_page = Site.find_for_request(request).root_page
    root_url = self.get_url_parts()[1]
    #entry_url = get_entry_url(self, self.blog_page.page_ptr, root_url)
    # use root_page instance, not root_url
    entry_url = get_entry_url(self, self.blog_page.page_ptr, root_page)
    return [
        {
            'location': root_url + entry_url,
            # fall back on latest_revision_created_at if last_published_at is null
            # (for backwards compatibility from before last_published_at was added)
            'lastmod': (self.last_published_at or self.latest_revision_created_at),
        }
    ]

setattr(EntryPage, 'get_sitemap_urls', get_sitemap_urls)