from django.urls import path
from explain import views


urlpatterns = [
    path('question', views.all_questions),
    path('newquestion', views.new_question),

]
