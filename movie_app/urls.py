from django.urls import path
from . import views

urlpatterns = [
    path('directors/', views.DirectorAPIView.as_view()),
    path('movies/', views.MovieAPIView.as_view()),
    path('reviews/', views.ReviewAPIView.as_view()),
    path('directors/<int:id>/', views.DirectorDetailAPIView.as_view()),
    path('movies/<int:id>/', views.MovieDetailAPIView.as_view()),
    path('reviews/<int:id>/', views.ReviewDetailAPIView.as_view()),
    path('directors/', views.directors_list),
    path('movies/reviews/', views.movie_reviews),
    path('directors/', views.DirectorListCreate),
    path('directors/<int:pk>/', views.DirectorRetrieveUpdateDestroy),
    path('movies/', views.MovieListCreate),
    path('movies/<int:pk>/', views.MovieRetrieveUpdateDestroy),
    path('reviews/', views.ReviewListCreate),
    path('reviews/<int:pk>/', views.DirectorRetrieveUpdateDestroy),

]
