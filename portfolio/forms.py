from django import forms
from .models import ContactMe


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMe
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'type': 'text', 'id': 'name', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'type': 'email', 'id': 'email', 'class': 'form-control'}),
            'message': forms.Textarea(attrs={'name': 'message', 'id': 'message', 'class': 'form-control', 'rows': '10'})
        }
