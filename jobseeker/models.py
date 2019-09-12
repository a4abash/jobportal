from django.db import models
from django.contrib.auth.models import User
#from phone_field import PhoneField
# Create your models here.
gender = (('male', 'Male'), ('female', 'Female'), ('other', 'Other'))
class JobSeeker(models.Model):
    address = models.CharField(max_length=100)
    experience_year = models.IntegerField(default=0, null=True, blank=True)
    cv = models.FileField(upload_to='cv/',null=True, blank=True)
    profile = models.ImageField(upload_to='profile/')
    professional_title = models.CharField(max_length=100, null=True, blank=True)
    contact_number = models.CharField(max_length=10)
    # contact_number = PhoneField(blank=True,null=True,unique=True)
    description = models.TextField(null=True, blank=True, help_text="About Yourself")
    url = models.URLField(blank=True, null=True)
    gender = models.CharField(choices=gender, max_length=10)
    qualification = models.CharField(max_length=100, help_text="Your Highest Degree")
    user= models.ForeignKey(User, on_delete=models.CASCADE,default=1)

    def __str__(self):
        return self.user.username

class Skill(models.Model):
    skill_title = models.CharField(max_length=100)
    proficiency_level = models.IntegerField()
    jobseeker = models.ForeignKey(JobSeeker, on_delete=models.CASCADE)

    def __str__(self):
        return self.skill_title

class Experience(models.Model):
    company = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    jobseeker = models.ForeignKey(JobSeeker, on_delete=models.CASCADE)

    def __str__(self):
        return self.jobseeker.user.username

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    link = models.URLField(null=True ,blank=True, unique=True)
    jobseeker = models.ForeignKey(JobSeeker, on_delete=models.CASCADE)

    def __str__(self):
        return self.jobseeker.user.username