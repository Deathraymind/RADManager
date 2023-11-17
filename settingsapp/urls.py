from django.urls import path
from . import views

app_name = 'settingsapp'
urlpatterns = [
    path('settings/', views.edit_settings, name='app_settings'),
    path('edit_settings/', views.edit_settings, name='edit_settings'),
    # Add more URL patterns for other views if needed
]
