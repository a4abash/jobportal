from django.urls import path
from . import views
urlpatterns = [
    path('create/', views.create, name='create_company'),  #
    path('vacancy-create/', views.vacancy_create, name='vacancy_create'),  # ADD/Post vacancy
    path('name-edit/', views.name_update, name="cname_update"),  # Updates the name of company
    path('vacancy-view/', views.vacancy_view, name='vacancy_view'),  # List all the added vacancies
    path('vacancy-view/<int:x>', views.vacancy_details, name='vacancy_details'),  # Provide the detail of particular task
    path('edit_cdescription', views.edit_cdescription, name='edit_cdescription'),  # Updates the description of company
    path('update_companyDetails/', views.update_companyDetails, name="update_companyDetails"),  # updates the detail of company
]