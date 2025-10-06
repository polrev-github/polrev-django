from django.db import models

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel


class FormsPage(Page):

    parent_page_types = ["home.HomePage"]
    subpage_types = [
        "forms.FormPage",
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context["forms"] = FormsPage.objects.all()


class FormPage(Page):

    form_url = models.URLField("form url", max_length=512)
    height = models.PositiveIntegerField(default=2000)

    parent_page_types = ["forms.FormsPage"]

    content_panels = Page.content_panels + [
        FieldPanel("form_url"),
        FieldPanel("height"),
    ]
