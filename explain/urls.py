from django.urls import path
from explain import views


urlpatterns = [
    path('allquestions', views.all_questions),
    path('getquestion/<int:id>', views.get_question),
    path('newquestion', views.new_question),
    path('answer/<int:id>', views.answers),
    path('new_answer', views.new_answer),

]
