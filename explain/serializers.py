from rest_framework import serializers

from .models import Answer, Comment, Question


class QuestionSerializerAllField (serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['question_id', 'question_title']


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
