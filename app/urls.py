from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.conf.urls import handler404, handler500


app_name = 'app'
urlpatterns = [
    path('profile/', views.create_profile, name='profile'),
    # path('invalid_input_profile/', views.create_profile, name='profile_redirect'),
    path('published_profile/<int:pk>',
         views.ProfileView.as_view(), name='published_profile'),
    path('home/', views.homepage, name='home'),
    path('update_profile/<int:pk>', views.update_profile, name='update_profile'),
    path('news_feed/', views.news_feed, name='news_feed'),
    path('messaging/', views.messaging, name='messaging'),
    path('friends/', views.friends, name='friends'),
    path('notifications/', views.notifications, name='notifications'),
    path('settings/', views.settings, name='settings'),
    path('endorse/<int:pk>', views.endorse, name='endorse')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
handler404 = views.error404
handler500 = views.error500
