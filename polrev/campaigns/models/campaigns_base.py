import usa

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from wagtail.models import Page
from wagtail.contrib.routable_page.models import RoutablePageMixin, route


class CampaignsPageBase(RoutablePageMixin, Page):
    class Meta:
        abstract = True

    @route(r"^state/(?P<state_slug>[-\w]*)", name="state_view")
    def state_view(self, request, state_slug):
        page = request.GET.get("page")
        name = state_slug.replace("-", " ")
        name = " ".join(i.capitalize() for i in name.split())
        if name == "District Of Columbia":
            name = "District of Columbia"
        state = usa.states.lookup(name, field="name")
        state_fips = state.fips
        campaigns = self.paginate(self.get_state_campaigns(state_fips), page)

        return self.render(
            request,
            context_overrides={
                "title": "State campaigns",
                "campaigns": campaigns,
            },
        )

    @route(r"^search/$")
    def post_search(self, request, *args, **kwargs):
        search_query = request.GET.get("q", None)
        page = request.GET.get("page")
        if search_query:
            campaigns = self.paginate(self.get_campaigns().search(search_query), page)
        else:
            campaigns = self.paginate(self.get_campaigns(), page)

        return self.render(
            request,
            context_overrides={
                "title": "Current campaigns",
                "campaigns": campaigns,
            },
        )

    def paginate(self, items, page):
        paginator = Paginator(items, 10)
        try:
            result = paginator.page(page)
        except PageNotAnInteger:
            result = paginator.page(1)
        except EmptyPage:
            result = paginator.object_list.none()
        return result

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        page = request.GET.get("page")
        context["states"] = usa.states.STATES_AND_TERRITORIES
        context["campaigns"] = self.paginate(self.get_campaigns(), page)

        return context
