from django.urls import path

from . import views

app_name = 'app'
urlpatterns = [
    #path('profile/', views.create_profile, name='profile'),
    path('profile/', views.create_profile, name='profile'),
    path('published_profile/<int:pk>', views.ProfileView.as_view(), name='published_profile'),
    path('news_feed/', views.news_feed, name='news_feed'),
    path('messaging/', views.messaging, name='messaging'),
    path('friends/', views.friends, name='friends'),
    path('notifications/', views.notifications, name='notifications'),
    path('settings/', views.settings, name='settings'),

]