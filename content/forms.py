from django import forms
from django.db.models.base import Model
from django.forms import fields
from .models import Contact

class ContactForm(forms.ModelForm):
    fullname = forms.CharField(required=True, max_length=100)
    email = forms.EmailField(required=True, max_length=254)
    phone_number = forms.CharField(required=True, max_length=15)
    subject = forms.CharField(required=True, max_length=250)
    message = forms.CharField(required=True, widget=forms.Textarea)

    class Meta:
        model = Contact
        fields = [
            "fullname",
            "email",
            "phone_number",
            "subject",
            "message",
        ]


    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields["fullname"].widget.attrs["placeholder"] = "Your Full Name"
        self.fields["fullname"].widget.attrs["class"] = "form-control form-control-lg"
        self.fields["email"].widget.attrs["placeholder"] = "Your email address"
        self.fields["email"].widget.attrs["class"] = "form-control form-control-sm"
        self.fields["phone_number"].widget.attrs["placeholder"] = "Your phone number"
        self.fields["phone_number"].widget.attrs["class"] = "form-control"
        self.fields["subject"].widget.attrs["placeholder"] = "Subject"
        self.fields["subject"].widget.attrs["class"] = "form-control form-control-sm"
        self.fields["message"].widget.attrs["placeholder"] = "Your Message"
        self.fields["message"].widget.attrs["cols"] = "30"
        self.fields["message"].widget.attrs["rows"] = "10"

        
