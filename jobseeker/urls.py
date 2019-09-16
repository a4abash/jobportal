from django.urls import path
from . import views
urlpatterns = [
    path('create/', views.create, name='create'),
    path('skill-create/',views.skill_store,name='skill_store'),
    path('exp-create/',views.exp_store,name='exp_store'),
    path('skill/delete/<int:x>',views.remove,name='skill_delete'),
    path('name-edit/',views.name_update,name="name_update"),
    path('details-edit/',views.details_update,name='details_update'),
    path('edit-project/<int:x>',views.edit_project,name='edit_project'),
]
