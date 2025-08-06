from django.urls import path
from . import views

app_name = 'api_services'

urlpatterns = [
    path('weather/', views.get_weather, name='weather'),
    path('news/', views.get_news, name='news'),
    path('quote/', views.get_quote, name='quote'),
    path('github/', views.get_github_stats, name='github-stats'),
    path('apod/', views.get_apod, name='get_apod'),
]
