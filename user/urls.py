from django.urls import path
from user import views

urlpatterns = [
    path('allusers', views.all_users),
    path('getuser/<int:id>', views.get_user),
    path('newuser', views.new_user),
]
