from django.urls import path
from . import views
urlpatterns = [
    path('create/', views.create, name='create'),
    path('skill-create/',views.skill_store,name='skill_store'),
    path('exp-create/',views.exp_store,name='exp_store'),
]