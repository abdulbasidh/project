from rest_framework import serializers
from django.contrib.auth.models import User
from accounts.models import Persons

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class PersonsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persons
        fields = ('id', 'username', 'email', 'password', 'phone')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        persons = Persons.objects.create_persons(validated_data['username'], validated_data['email'], validated_data['phone'], validated_data['password'])

        return persons

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user
