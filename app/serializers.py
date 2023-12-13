import bcrypt
from rest_framework import serializers
from .models import *

# READ USERS SERIALIZER
class UsersListSerializer(serializers.ModelSerializer):
    team_name = serializers.SerializerMethodField()

    class Meta:
        model = Users
        fields = ['id', 'username', 'team_name', 'created', 'updated']

    def get_team_name(self, user):
        return user.team.name if user.team else None

# CREATE USERS SERIALIZER   
class UsersCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['username', 'password', 'isAdmin']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        if 'password' in validated_data:
            salt = bcrypt.gensalt()
            hashed_password = bcrypt.hashpw(validated_data['password'].encode('utf-8'), salt)
            validated_data['password'] = hashed_password.decode('utf-8')

        return super().create(validated_data)

# UPDATE USERS SERIALIZER
class UsersUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['username', 'password', 'isAdmin']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            salt = bcrypt.gensalt()
            hashed_password = bcrypt.hashpw(validated_data['password'].encode('utf-8'), salt)
            validated_data['password'] = hashed_password.decode('utf-8')

        return super().update(instance, validated_data)