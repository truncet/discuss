
from os import name

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('explain/', include('explain.urls')),
    path('user/', include('user.urls', namespace='users')),
    path('auth/', include('drf_social_oauth2.urls', namespace='drf')),


]
