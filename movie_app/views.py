from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Movie, Director, Review
from .serializers import MovieSerializer, DirectorSerializer, ReviewSerializer
from rest_framework import status

@api_view(['GET'])
def director_list_api_view(request):
    if request.method == 'GET':
        queryset = Director.objects.all()
        serializer = DirectorSerializer(queryset, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

@api_view(['GET'])
def director_detail_api_view(request, id):
    if request.method == 'GET':
        queryset = Director.objects.get(id=id)
        serializer = DirectorSerializer(queryset)
        return Response(serializer.data)

@api_view(['GET'])
def movie_list_api_view(request):
    if request.method == 'GET':
        queryset = Movie.objects.all()
        serializer = MovieSerializer(queryset)
        return Response(serializer.data)

@api_view(['GET'])
def movie_detail_api_view(request, id):
    if request.method == 'GET':
        queryset = Movie.objects.get(id=id)
        serializer = MovieSerializer(queryset)
        return Response(serializer.data)

@api_view(['GET'])
def review_list_api_view(request):
    if request.method == 'GET':
        queryset = Review.objects.all()
        serializer = ReviewSerializer(queryset)
        return Response(serializer.data)

@api_view(['GET'])
def review_detail_api_view(request, id):
    if request.method == 'GET':
        queryset = Review.objects.get(id=id)
        serializer = ReviewSerializer(queryset)
        return Response(serializer.data)
