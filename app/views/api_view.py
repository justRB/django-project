import random
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, generics
from app.models import Users
from app.serializers import *


# READ USER
class APIUsersView(APIView):
    def get(self, request, id):
        try:
            user = Users.objects.get(id=id)
            serializer = UsersListSerializer(user)
            return Response(serializer.data)
        except Exception:
            return Response(status=status.HTTP_404_NOT_FOUND)

# READ USERS
class ApiUsersList(APIView):
    def get(self, request):
            users = Users.objects.all()
            serializer = UsersListSerializer(users, many=True)
            return Response(serializer.data)
    
# CREATE USER
class ApiUsersCreate(APIView):
    def post(self, request):
            serializer = UsersCreateSerializer(data=request.data)
            if (serializer.is_valid()):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
# DELETE USER
class APIUsersDelete(generics.DestroyAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersListSerializer
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            self.perform_destroy(instance)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
# UPDATE USER
class APIUsersUpdate(APIView):
     def post(self, request, id):
        user = Users.objects.get(id=id)
        
        serializer = UsersUpdateSerializer(user, data=request.data, partial=True)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
     
# RESET TEAMS TO USERS   
class APIUsersReset(APIView):
     def get(self, request):  
        try:
            users = list(Users.objects.all())

            for user in users:
                user.team = None
                user.save()

            serializer = UsersListSerializer(users, many=True)           
    
            return Response(serializer.data, status=status.HTTP_200_OK) 
        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# ADD TEAMS TO USERS
class APIUsersShuffle(APIView):
    def get(self, request):
        try:
            users = list(Users.objects.all())
            teams = Teams.objects.all()

            teams_ids = list(teams.values_list('id', flat=True))
            random.shuffle(teams_ids)
            random.shuffle(users)

            index = 0
            for user in users:
                user.team = Teams.objects.get(id=teams_ids[index])
                user.save()

                if (index + 1) < len(teams_ids):
                    index += 1
                else:
                    index = 0

            serializer = UsersListSerializer(users, many=True)
                
            return  Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
# READ TEAM
class APITeamsView(APIView):
    def get(self, request, id):
        try:

            team = Teams.objects.get(id=id)
            serializer = TeamsListSerializer(team)
            return Response(serializer.data)
        except Exception:
            return Response(status=status.HTTP_404_NOT_FOUND)

# READ TEAMS
class APITeamsList(APIView):
    def get(self, request):
        teams = Teams.objects.all()
        serializer = TeamsListSerializer(teams, many=True)
        return Response(serializer.data)
    
# CREATE TEAM
class APITeamsCreate(APIView):
    def post(self, request):
        serializer = TeamsCreateUpdateSerializer(data=request.data)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

# DELETE TEAM
class APITeamsDelete(generics.DestroyAPIView):
    queryset = Teams.objects.all()
    serializer_class = TeamsListSerializer
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            self.perform_destroy(instance)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception:
            return Response(status=status.HTTP_404_NOT_FOUND)

# UPDATE TEAM
class APITeamsUpdate(APIView):
    def post(self, request, id):
        team = Teams.objects.get(id=id)

        serializer = TeamsCreateUpdateSerializer(team, data=request.data, partial=False)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)