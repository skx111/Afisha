from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Movie, Director, Review
from .serializers import MovieSerializer, DirectorSerializer, ReviewSerializer
from rest_framework import status
from django.db.models import Avg, Count
from django.http import JsonResponse


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
def review_detail_api_view(request):
    if request.method == 'GET':
        queryset = Review.objects.get(id=id)
        serializer = ReviewSerializer(queryset)
        return Response(serializer.data)


def movie_reviews(request):
    movies = Movie.objects.prefetch_related('review_set').all()
    movie_data = []

    total_reviews = 0
    total_rating = 0

    for movie in movies:
        reviews = movie.review_set.all()
        average_rating = reviews.aggregate(Avg('stars'))['stars__avg']
        total_reviews += reviews.count()
        total_rating += average_rating or 0

        movie_data.append({
            'title': movie.title,
            'reviews': [{'text': review.text, 'stars': review.stars} for review in reviews],
            'average_rating': average_rating or 0
        })

    overall_average_rating = total_rating / total_reviews if total_reviews > 0 else 0

    return JsonResponse({'movies': movie_data, 'overall_average_rating': overall_average_rating})

def directors_list(request):
    directors = Director.objects.annotate(movies_count=Count('movie')).values('name', 'movies_count')
    return JsonResponse({'directors': list(directors)})