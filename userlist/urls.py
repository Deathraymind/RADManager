from django.urls import path


from . import views

urlpatterns = [
    path('list_users/', views.list_users, name='list_users'),
    path('reset_password/<str:username>/', views.reset_password, name='reset_password'),
    # Other URL patterns if needed
]
