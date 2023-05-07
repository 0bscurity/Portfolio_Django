from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control bg-dark text-white mb-3'}), required=True)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control bg-dark text-white mb-4'}), required=True)
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control bg-dark text-white mb-3', 'rows': '3'}), required=True)