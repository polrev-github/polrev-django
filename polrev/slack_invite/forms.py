from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit

class InviteForm(forms.Form):
    email_addr = forms.EmailField(
        widget=forms.EmailInput(
            attrs={'class':'form-signin input','placeholder':'Email address'}
            ),
            label='',
            required=True
        )
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_class = 'form'

        self.helper.add_input(Submit('submit', 'Join Team!', css_class='btn-block btn-inset'))