from .models import ContactMessage
from django import forms
 
# creating a form
class ContactForm(forms.ModelForm):
 
    # create meta class
    class Meta:
        # specify model to be used
        model = ContactMessage
 
        # specify fields to be used
        fields = [
            "name",
            "email",
            "subject",
            "message",
        ]