from django.db import models

# Create your models here.


class Entity(models.Model):
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
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    best_answer = models.BooleanField(default=False)


class Comment(Entity):
    comment_id = models.BigAutoField(primary_key=True)
    question_parent_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_parent_id = models.ForeignKey(Answer, on_delete=models.CASCADE)
