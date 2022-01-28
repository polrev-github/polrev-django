from django.utils.safestring import mark_safe

from wagtail.admin.edit_handlers import EditHandler
from django.template.loader import render_to_string

#Todo:Hacky
from birdsong.models import Contact

class PreviewPanel(EditHandler):
    def render(self):
        #print(self.__dict__)

        first_receipt = self.instance.receipts.first()
        if first_receipt:
            #preview_contact = self.contact_class.objects.filter(
            preview_contact = Contact.objects.filter(
            pk=first_receipt.pk).first()
        else:
            preview_contact = None

        preview = render_to_string(
            self.instance.get_template(self.request),
            self.instance.get_context(self.request, preview_contact),
        )

        return mark_safe(f"<fieldset>{preview}</fieldset>")
