from django.db import models

# Create your models here.


class Slider(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='slider/')

    def __str__(self):
        return self.title


class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField()
    company = models.CharField(max_length=100, null=True, blank=True)
    designation = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name