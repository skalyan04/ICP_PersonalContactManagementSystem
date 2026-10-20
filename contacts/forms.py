from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["name", "birthday", "address", "phone", "email"]
        error_messages = {
            "phone": {
                "required": "Please enter a phone number.",
            },
        }
        widgets = {
            "birthday": forms.DateInput(attrs={"type": "date"}),
        }
