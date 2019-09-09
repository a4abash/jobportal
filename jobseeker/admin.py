from django.contrib import admin
from .models import JobSeeker, Skill, Experience, Project
# Register your models here.
admin.site.register(JobSeeker)
admin.site.register(Skill)
admin.site.register(Experience)
admin.site.register(Project)

