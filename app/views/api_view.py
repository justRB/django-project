from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from app.models import Users
from app.serializers import *

# GET Users list
class ApiUsersList(APIView):
    def get(self, request):
            users = Users.objects.all()
            serializer = UsersListSerializer(users, many=True)
            return Response(serializer.data)
    
# POST Add user
class ApiUsersCreate(APIView):
    def post(self, request):
            serializer = UsersListSerializer(data=request.data)
            if (serializer.is_valid()):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)