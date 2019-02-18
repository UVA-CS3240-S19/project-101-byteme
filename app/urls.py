from django.urls import path

from . import views

app_name = 'app'
urlpatterns = [
    #path('profile/', views.create_profile, name='profile'),
    path('profile/', views.create_profile, name='profile'),
    path('published_profile/', views.ProfileView.as_view(), name='published_profile')
]