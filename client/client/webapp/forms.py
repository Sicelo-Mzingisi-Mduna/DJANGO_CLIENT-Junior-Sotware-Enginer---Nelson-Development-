from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class ValidationForm(forms.Form):
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={"class": "form-control"}))
    url = forms.URLField(label="API Endpoint URL", widget=forms.URLInput(attrs={"class": "form-control"}))

    def __init__(self, *args, **kwargs): # type: ignore
        super(ValidationForm, self).__init__(*args, **kwargs) # type: ignore
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Validate'))  # type: ignore
