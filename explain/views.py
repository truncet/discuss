from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from explain.models import Answer, Comment, Question
from explain.serializers import AnswerSerializer, QuestionSerializer

# Create your views here.


@api_view(['GET'])
def all_questions(request):
    questions = Question.objects.all()
    serializer = QuestionSerializer(questions, many=True)

    return JsonResponse({"data": serializer.data})


@api_view(['GET'])
def get_question(request, id):
    question = Question.objects.filter(question_id=id)
    serializer = QuestionSerializer(question, many=True)

    return JsonResponse({"data": serializer.data})


@api_view(['POST'])
def new_question(request):
    serializerd_questions = QuestionSerializer(data=request.data)

    if (serializerd_questions.is_valid()):
        serializerd_questions.save()

    return Response({"data": serializerd_questions.data})


@api_view(['GET'])
def answers(request, id):
    answers = Answer.objects.filter(question_id=id)
    print(answers)
    serializer = AnswerSerializer(answers, many=True)

    return JsonResponse({"data": serializer.data})


@api_view(['POST'])
def new_answer(request):
    serialized_answers = AnswerSerializer(data=request.data)
    if (serialized_answers.is_valid()):
        serialized_answers.save()
    else:
        print("could not validate")

    return Response({"data": serialized_answers.data})
