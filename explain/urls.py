from django.urls import path

from explain import views

urlpatterns = [
    # path('allquestions', views.all_questions),
    # path('getquestion/<int:id>', views.get_question),
    # path('newquestion', views.new_question),
    # path('answer/<int:id>', views.answers),
    # path('newanswer', views.new_answer),
    path('question/<int:pk>', views.Questions.as_view()),
    path('allquestions', views.AllQuestions.as_view()),
]
