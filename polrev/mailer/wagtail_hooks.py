from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register

from birdsong.options import CampaignAdmin
from birdsong.models import Contact
from .models import Newsletter

'''
@modeladmin_register
class ContactAdmin(ModelAdmin):
    model = ExtendedContact
    menu_label = 'Contacts'
    menu_icon = 'user'
    list_diplay = ('email', 'first_name', 'last_name', 'location')
'''

@modeladmin_register
class ContactAdmin(ModelAdmin):
    model = Contact
    menu_label = 'Contacts'
    menu_icon = 'user'
    list_diplay = ('email')

@modeladmin_register
class NewsletterAdmin(CampaignAdmin):
    campaign = Newsletter
    menu_label = 'Newsletter'
    menu_icon = 'mail'
    menu_order = 1000
    #form_view_extra_js = ['birdsong_fix/js/preview_campaign.js']
    form_view_extra_js = None
    #form_view_extra_css = ['birdsong_fix/css/campaign-editor.css']
    form_view_extra_css = None
