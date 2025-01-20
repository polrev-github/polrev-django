from django import forms

from areas.models import Area


class AreaForm(forms.ModelForm):
    class Meta:
        model = Area
        fields = ["name", "title"]
