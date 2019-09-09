from django import forms
from .models import Company

class CompanyForm(forms.ModelForm):

    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    contact = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    website = forms.URLField(widget=forms.URLInput  (attrs={'class':'form-control'}))
    company_type = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))

    class Meta:
        model = Company
        exclude = ['user']