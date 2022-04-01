from django import forms

from offices.models import OfficeType, Office, StateOfficeBase

class OfficeTypeForm(forms.ModelForm):
    class Meta:
        model = OfficeType
        fields = ['title']

class OfficeForm(forms.ModelForm):
    class Meta:
        model = Office
        fields = ['type_ref', 'title', 'website']

class FederalOfficeForm(OfficeForm):
    pass

class StateOfficeBaseForm(OfficeForm):
    class Meta:
        model = StateOfficeBase
        fields = OfficeForm.Meta.fields + ['state_ref']
