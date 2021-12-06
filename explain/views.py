import json

from django.http import JsonResponse
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from explain.models import Answer, Comment, Question
from explain.serializers import AnswerSerializer, QuestionSerializer, QuestionSerializerAllField

# Create your views here.


# @api_view(['GET'])
# def all_questions(request):
#     questions = Question.objects.all()
#     serializer = QuestionSerializer(questions, many=True)

#     return JsonResponse({"data": serializer.data})


# @api_view(['GET'])
# def get_question(request, id):
#     question = Question.objects.filter(question_id=id)
#     serializer = QuestionSerializer(question, many=True)

#     return JsonResponse({"data": serializer.data})


# @api_view(['POST'])
# def new_question(request):
#     serializerd_questions = QuestionSerializer(data=request.data)

#     if (serializerd_questions.is_valid()):
#         serializerd_questions.save()

#     return Response({"data": serializerd_questions.data})


# @api_view(['GET'])
# def answers(request, id):
#     answers = Answer.objects.filter(question_id=id)
#     print(answers)
#     serializer = AnswerSerializer(answers, many=True)

#     return JsonResponse({"data": serializer.data})


# @api_view(['POST'])
# def new_answer(request):
#     serialized_answers = AnswerSerializer(data=request.data)
#     if (serialized_answers.is_valid()):
#         serialized_answers.save()
#     else:
#         print("could not validate")

#     return Response({"data": serialized_answers.data})


class Questions (APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        question = Question.questions.filter(question_id=pk)
        serialized_question = QuestionSerializerAllField(question, many=True)
        return Response(serialized_question.data)

    def post(self, request):
        question = Answer.objects.all()
        print('This is post method')
        return Response(json.dumps({"message": "this is post"}))

    def put(self, request):
        print("This is put method ")
        return Response(json.dumps({"message": "this is put"}))

    def patch(self, request):
        print("this is patch method")
        return Response(json.dumps({"message": "this is patch"}))


class AllQuestions(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        question = Question.questions.all().values("question_id", "question_title")
        serialized_question = QuestionSerializer(question, many=True)
        return Response(serialized_question.data)
