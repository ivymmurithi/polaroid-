from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('register/',views.register,name='register'),
    path('', include('django.contrib.auth.urls')),
    path('',views.index, name='index'),
    path('results/', views.results, name='results'),
    path('profile/',views.profile, name='profile'),
    path('likes/', views.likes, name='likes'),
    path('comment/', views.comment, name='comment'),
    path('logoutuser/', views.logoutuser, name='logoutuser'),
    path('uploadprofile/', views.uploadprofile, name='uploadprofile'),
]


"""
new static route that references the location to the uploaded files
"""
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)