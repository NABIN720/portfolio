from django.urls import path
from . import views

app_name = 'portfolioapp'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('projects/<int:pk>/', views.project_detail, name='project_detail'),
    path('contact/', views.contact, name='contact'),
    path('productivity/', views.productivity_dashboard, name='productivity'),
]
