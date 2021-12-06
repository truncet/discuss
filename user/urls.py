from django.urls import path

from .views import CustomUserCreate, ShowCustomer

# urlpatterns = [
#     path('allusers', views.all_users),
#     path('getuser/<int:id>', views.get_user),
#     path('newuser', views.new_user),
# ]

app_name = 'users'
urlpatterns = [
    path('create/', CustomUserCreate.as_view(), name='create_user'),
    path('show', ShowCustomer.as_view(), name='show_user'),
]
