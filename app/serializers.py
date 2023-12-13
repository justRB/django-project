from rest_framework import serializers
from .models import *

class UsersListSerializer(serializers.ModelSerializer):
    team_name = serializers.SerializerMethodField()

    class Meta:
        model = Users
        fields = ['id', 'username', 'team_name', 'created', 'updated']

    def get_team_name(self, user):
        return user.team.name if user.team else None
    
class UsersCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['username', 'password', 'isAdmin']