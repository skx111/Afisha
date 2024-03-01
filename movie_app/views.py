from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.response import Response
from .models import Movie, Director, Review
from .serializers import MovieSerializer, DirectorSerializer, ReviewSerializer
from rest_framework import status
from django.db.models import Avg, Count
from django.http import JsonResponse, HttpResponseBadRequest
from django.shortcuts import get_object_or_404



@api_view(['GET', 'POST'])
def director_list_api_view(request):
    if request.method == 'GET':
        queryset = Director.objects.all()
        serializer = DirectorSerializer(queryset, many=True)
        return Response(serializer.data, status=200)
    elif request.method == 'POST':
        serializer = DirectorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=200)

@api_view(['GET', 'PUT', 'DELETE'])
def director_detail_api_view(request, id):
    queryset = Director.objects.get(id=id)
    if request.method == 'GET':
        serializer = DirectorSerializer(queryset)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = DirectorSerializer(queryset, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)
    elif request.method == 'DELETE':
        queryset.delete()
        return Response(status=204)


class DirectorListCreate(generics.ListCreateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer

class DirectorRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer

@api_view(['GET'])
def movie_list_api_view(request):
    if request.method == 'GET':
        queryset = Movie.objects.all()
        serializer = MovieSerializer(queryset)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = MovieSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=200)

@api_view(['GET'])
def movie_detail_api_view(request, id):
    queryset = Movie.objects.get(id=id)
    if request.method == 'GET':
        serializer = MovieSerializer(queryset)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = MovieSerializer(queryset, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)
    elif request.method == 'DELETE':
        queryset.delete()
        return Response(status=204)

class MovieListCreate(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

@api_view(['GET'])
def review_list_api_view(request):
    if request.method == 'GET':
        queryset = Review.objects.all()
        serializer = ReviewSerializer(queryset)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ReviewSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=200)

@api_view(['GET'])
def review_detail_api_view(request):
    queryset = Review.objects.get(id=id)
    if request.method == 'GET':
        serializer = ReviewSerializer(queryset)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ReviewSerializer(queryset, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)
    elif request.method == 'DELETE':
        queryset.delete()
        return Response(status=204)

class ReviewListCreate(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer



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



def validate_director_id(func):
    def wrapper(request, *args, **kwargs):
        director_id = kwargs.get('id')
        if director_id is None:
            return HttpResponseBadRequest('Director ID is required')
        if not Director.objects.filter(pk=director_id).exists():
            return HttpResponseBadRequest('Invalid Director ID')
        return func(request, *args, **kwargs)
    return wrapper

def validate_movie_id(func):
    def wrapper(request, *args, **kwargs):
        movie_id = kwargs.get('id')
        if movie_id is None:
            return HttpResponseBadRequest('Movie ID is required')
        if not Movie.objects.filter(pk=movie_id).exists():
            return HttpResponseBadRequest('Invalid Movie ID')
        return func(request, *args, **kwargs)
    return wrapper

def validate_review_id(func):
    def wrapper(request, *args, **kwargs):
        review_id = kwargs.get('id')
        if review_id is None:
            return HttpResponseBadRequest('Review ID is required')
        if not Review.objects.filter(pk=review_id).exists():
            return HttpResponseBadRequest('Invalid Review ID')
        return func(request, *args, **kwargs)
    return wrapper

def directors_list(request):
    directors = Director.objects.annotate(movies_count=Count('movie')).values('name', 'movies_count')
    return JsonResponse({'directors': list(directors)})

@validate_director_id
def director_detail(request, id):
    director = get_object_or_404(Director, pk=id)
    data = {'id': director.id, 'name': director.name}
    return JsonResponse(data)

def movies_list(request):
    movies = Movie.objects.all()
    data = [{'id': movie.id, 'title': movie.title} for movie in movies]
    return JsonResponse({'movies': data})

@validate_movie_id
def movie_detail(request, id):
    movie = get_object_or_404(Movie, pk=id)
    data = {
        'id': movie.id,
        'title': movie.title,
        'description': movie.description,
        'duration': movie.duration,
        'director': movie.director.name
    }
    return JsonResponse(data)

def reviews_list(request):
    reviews = Review.objects.all()
    data = [{'id': review.id, 'text': review.text} for review in reviews]
    return JsonResponse({'reviews': data})

@validate_review_id
def review_detail(request, id):
    review = get_object_or_404(Review, pk=id)
    data = {'id': review.id, 'text': review.text}
    return JsonResponse(data)