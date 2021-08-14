from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from user.serializers import UserSerializer
from user.models import User
# Create your views here.


@api_view(['GET'])
def all_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)

    return JsonResponse({"data": serializer.data})


@api_view(['GET'])
def get_user(request, id):
    user = User.objects.filter(user_id=id)
    serializer = UserSerializer(user, many=True)

    return JsonResponse({"data": serializer.data})


@api_view(['POST'])
def new_user(request):
    serialized_user = UserSerializer(data=request.data)

    if(serialized_user.is_valid()):
        serialized_user.save()
    else:
        print('could not validate')

    return Response({"data": serialized_user.data})


@api_view(['PUT'])
def update_user(request):
    serialized_user = UserSerializer(data=request.data)

    if(serialized_user.is_valid()):
        serialized_user.save()
    else:
        print("could not validate data")

    return Response({"data": serialized_user.data})
