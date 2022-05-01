from urllib import response
from django.shortcuts import render
from itsdangerous import Serializer
import requests
from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Movie
from .serializers import MovieSerializer,UserSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser, BasePermission
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.authtoken.models import Token

# list all movies in db
class MovieListView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request):
        Movies = Movie.objects.all()
        serializer = MovieSerializer(Movies,many=True)
        return Response(serializer.data)
        
    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

# add a movie from TMDB API db using its movie id to our local db
class AddMovie(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self,request,pk):
        tmdbRequest = requests.get("https://api.themoviedb.org/3/movie/"+str(pk),
                                   params={"api_key":"659ca4fbd788fe4c4a83a3d6a6f4275a"}).json()
        serializer = MovieSerializer(data=tmdbRequest)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
# register a user 
class RegisterUser(APIView):
    def post(self,request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            content = {'message': 'created successfully'}
            return Response(content)
        else:
            return Response(serializer.errors)

# get rating of a movie using movie id or rate a movie using put request      
class RatingMovie(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get_movie(self,pk):
        try:
            return Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            raise Http404
        
    def get(self,request,pk):
        movie = self.get_movie(pk)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    def put(self,request,pk):
        movie = self.get_movie(pk)
        serializer = MovieSerializer(movie,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response (serializer.errors)
                   
                   
        
        