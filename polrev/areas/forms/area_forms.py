from django import forms

from areas.models import Area
 
class AreaForm(forms.ModelForm):
    class Meta:
        model = Area
        fields = ['name', 'title']

'''
class FederalAreaForm(AreaForm):
    pass

class StateAreaForm(AreaForm):
    class Meta:
        model = StateOfficeBase
        fields = AreaForm.Meta.fields + ['state_ref']
'''