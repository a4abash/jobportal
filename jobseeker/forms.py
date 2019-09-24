from django import forms
from .models import JobSeeker, Project, Skill, Experience


# Designinig the Jobseeker form
class JobSeekerForm(forms.ModelForm):
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    profile = forms.ImageField
    experience_year = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    professional_title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    contact_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    url = forms.URLField(widget=forms.URLInput(attrs={'class': 'form-control'}))
    gender = forms.CharField(widget=forms.Select(choices=(('male', 'Male'), ('female', 'Female'), ('other', 'Other')),
                                                 attrs={'class': 'form-control'}))
    qualification = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = JobSeeker
        exclude = ['user']


# Used to change the profile picture of Jobseeker
class ProfileImageForm(forms.ModelForm):
    class Meta:
        model = JobSeeker
        fields = ['profile']


# Designinig the Jobseeker form called by name jform
class JobSeekerUpdateForm(forms.ModelForm):
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    experience_year = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    professional_title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    contact_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    url = forms.URLField(widget=forms.URLInput(attrs={'class': 'form-control'}))
    gender = forms.CharField(widget=forms.Select(choices=(('male', 'Male'), ('female', 'Female'), ('other', 'Other')),
                                                 attrs={'class': 'form-control'}))
    qualification = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = JobSeeker
        fields = ['professional_title', 'url', 'contact_number', 'address', 'gender', 'qualification','experience_year']


# Designinig the Skill form called by name sform
class SkillForm(forms.ModelForm):
    skill_title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    proficiency_level = forms.CharField(widget=forms.NumberInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Skill
        exclude = ('jobseeker',)


# Designinig the Project form called by jobseeker_project_form'
class JobSeekerProjectForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    link = forms.URLField(widget=forms.URLInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Project
        exclude = ('jobseeker',)


# Designinig the Experience form called by name expform
class ExperienceForm(forms.ModelForm):
    company = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    post = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    start_date = forms.CharField(widget=forms.DateInput(attrs={'class': 'form-control'}))
    end_date = forms.CharField(widget=forms.DateInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Experience
        exclude = ('jobseeker',)


# Designinig the Jobseeker form called by name dform
class JobseekerDescriptionUpdateForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))

    class Meta:
        model = JobSeeker
        fields = ['description']



