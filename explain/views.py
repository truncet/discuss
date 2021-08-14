from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework. response import Response
from explain.serializers import QuestionSerializer
from explain.models import Question

# Create your views here.


@api_view(['GET'])
def all_questions(request):
    questions = Question.objects.all()
    serializer = QuestionSerializer(questions, many=True)

    return JsonResponse(serializer.data, safe=False)


@api_view(['POST'])
def new_question(request):
    serializerd_questions = QuestionSerializer(data=request.data)

    if (serializerd_questions.is_valid()):
        serializerd_questions.save()

    return Response(serializerd_questions.data)
