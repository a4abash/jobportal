from django.db import models
from django.contrib.auth.models import User
#from phone_field import PhoneField


# Create your models here.
# adds object Company to company with mentioned properties
class Company(models.Model):
    address = models.CharField(max_length=100)
    # contact = PhoneField(uniques=True)
    contact = models.CharField(max_length=10)
    website = models.URLField(null=True, blank=True, unique=True)
    company_type = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


# adds object Job to company with mentioned properties
class Job(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='image/', null=True, blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
