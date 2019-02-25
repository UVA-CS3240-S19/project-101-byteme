"""skimatch URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name = 'main_page'),
    path('sign_up/', views.sign_up, name = 'sign_up'),
    path('profile/', views.create_profile, name = 'profile'),
    path('published_profile/', views.ProfileView.as_view(), name='published_profile'),
    path('news_feed/', views.news_feed, name='news_feed'),
    path('messaging/', views.messaging, name='messaging'),
    path('friends/', views.friends, name='friends'),
    path('notifications/', views.notifications, name='notifications'),
    path('settings/', views.settings, name='settings'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
