from dataclasses import fields
from .models import Movie
from django.contrib.auth.models import User
from rest_framework import serializers

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id','title','vote_average','local_rating']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password','email']
        
        