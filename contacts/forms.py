from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["name", "birthday", "address", "phone", "email"]
        widgets = {
            "birthday": forms.DateInput(attrs={"type": "date"}),
        }
