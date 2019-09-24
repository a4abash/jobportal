from django import forms
from .models import Company, Job


# Designing the Company form called in company/views by 'form'
class CompanyForm(forms.ModelForm):
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    contact = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    website = forms.URLField(widget=forms.URLInput(attrs={'class': 'form-control'}))
    company_type = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))

    class Meta:
        model = Company
        exclude = ['user']


# Designinig the Company form called by name jform
class CompanyDetailUpdateForm(forms.ModelForm):
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    contact = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    website = forms.URLField(widget=forms.URLInput(attrs={'class': 'form-control'}))
    company_type = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Company
        exclude = ['user', 'description']


# Designinig the Company form called by name jform
class JobForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
    image = forms.ImageField

    class Meta:
        model = Job
        exclude = ['company']


# Designinig the Company form called by name jform
class CompanyUpdateDescription(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))

    class Meta:
        model = Company
        fields = ['description']