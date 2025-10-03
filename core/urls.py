from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.save_contact, name='contact'),
    path('projects/', views.project_list, name='projects'),
    path('projects/<int:project_id>/', views.project_detail, name='project_detail'),
]
