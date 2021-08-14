from django.db import models

from user.models import User

# Create your models here.


class Entity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Question(Entity):
    question_id = models.BigAutoField(primary_key=True)
    question_title = models.CharField(max_length=200)
    question_description = models.CharField(max_length=2000)


class Answer(Entity):
    answer_id = models.BigAutoField(primary_key=True)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_description = models.CharField(max_length=2000)
    best_answer = models.BooleanField(default=False)


class Comment(Entity):
    comment_id = models.BigAutoField(primary_key=True)
    question_parent_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_parent_id = models.ForeignKey(Answer, on_delete=models.CASCADE)
    comment = models.CharField(max_length=2000)
