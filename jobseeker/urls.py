from django.urls import path
from . import views
urlpatterns = [
    path('create/', views.create, name='create'),  # calls the jobseeker creation form jobseeker/view
    path('edit-profile', views.edit_profile, name='edit_profile'),  # Post method for user profile picture update
    path('name-edit/', views.name_update, name="name_update"),  # Jobseeker first name and last name section
    path('details-edit/', views.details_update, name='details_update'),  # Jobseeker details update section
    path('skill-create/', views.skill_store, name='skill_store'),  # Jobseeker skills update section
    path('skill/delete/<int:x>', views.remove, name='skill_delete'),  # Jobseeker skill delete
    path('edit-description', views.edit_description, name='edit_description'),  # Jobseeker description edit section
    path('edit-project/<int:x>', views.edit_project, name='edit_project'),  # project edit section
    path('project/delete/<int:x>', views.rmvprj, name='rmvprj'),  # removes each project from project table at a time
    path('experience-add/', views.experience_add, name='experience_add'),  # adds experience of user to Experience table

    path('experience/delete/<int:x>', views.exp_dlt, name='exp_dlt'),  # delete the data from experience table
]
#     path('experience-edit/<int:x>', views.exp_edit, name='exp_edit'),  # edits the experience table
