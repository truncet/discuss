
from django.contrib.auth.models import PermissionsMixin
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import CustomUserSerializer

#from user.serializers import UserSerializer

# Create your views here.


# @api_view(['GET'])
# def all_users(request):
#     users = User.objects.all()
#     serializer = UserSerializer(users, many=True)

#     return JsonResponse({"data": serializer.data})


# @api_view(['GET'])
# def get_user(request, id):
#     user = User.objects.filter(user_id=id)
#     serializer = UserSerializer(user, many=True)

#     return JsonResponse({"data": serializer.data})


# @api_view(['POST'])
# def new_user(request):
#     serialized_user = UserSerializer(data=request.data)

#     if(serialized_user.is_valid()):
#         serialized_user.save()
#     else:
#         print('could not validate')

#     return Response({"data": serialized_user.data})


# @api_view(['PUT'])
# def update_user(request):
#     serialized_user = UserSerializer(data=request.data)

#     if(serialized_user.is_valid()):
#         serialized_user.save()
#     else:
#         print("could not validate data")

#     return Response({"data": serialized_user.data})

class CustomUserCreate(APIView):
    permission_classes = [AllowAny]

    def post(self, request, format='json'):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
