
from os import name
from django.contrib import admin
from django.urls import include, path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('explain/', include('explain.urls')),
    path('user/', include('user.urls', namespace='users')),
    path('get/token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('get/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
]
