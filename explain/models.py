from django.conf import settings
from django.db import models

# Create your models here.


class Entity(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,   on_delete=models.CASCADE)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class QuestionManager(models.Manager):
    def get_queryset(self):
        return super(QuestionManager, self).get_queryset()


class Question(Entity):
    question_id = models.BigAutoField(primary_key=True)
    question_title = models.TextField(max_length=200)
    question_description = models.TextField(max_length=2000)
    questions = QuestionManager()


class Answer(Entity):
    answer_id = models.BigAutoField(primary_key=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_description = models.TextField(max_length=2000)
    best_answer = models.BooleanField(default=False)


class Comment(Entity):
    comment_id = models.BigAutoField(primary_key=True)
    question_parent = models.ForeignKey(
        Question, on_delete=models.CASCADE, null=True, blank=True)
    answer_parent = models.ForeignKey(
        Answer, on_delete=models.CASCADE, null=True, blank=True)
    comment = models.TextField(max_length=2000)
