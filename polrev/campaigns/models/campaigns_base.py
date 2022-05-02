import us

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from wagtail.core.models import Page
from wagtail.contrib.routable_page.models import RoutablePageMixin, route

class CampaignsPageBase(RoutablePageMixin, Page):
    class Meta:
        abstract = True

    @route(r"^state/(?P<state_slug>[-\w]*)", name="state_view")
    def state_view(self, request, state_slug):
        name = state_slug.replace('-', ' ')
        name = ' '.join(i.capitalize() for i in name.split())
        state = us.states.lookup(name, field='name')
        state_fips = state.fips
        campaigns = self.get_state_campaigns(state_fips)

        return self.render(request, context_overrides={
            'title': "State campaigns",
            'campaigns': campaigns,
        })

    @route(r"^search/$")
    def post_search(self, request, *args, **kwargs):
        search_query = request.GET.get("q", None)
        campaigns = self.get_campaigns()
        if search_query:
            campaigns = campaigns.search(search_query)
        return self.render(request, context_overrides={
            'title': "Current campaigns",
            'campaigns': campaigns,
        })

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['states'] = us.states.STATES

        paginator = Paginator(self.get_campaigns(), 10)
        page = request.GET.get("page")
        try:
            campaigns = paginator.page(page)
        except PageNotAnInteger:
            campaigns = paginator.page(1)
        except EmptyPage:
            campaigns = paginator.object_list.none()

        context["campaigns"] = campaigns

        return context
