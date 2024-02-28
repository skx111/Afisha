from django.urls import path
from . import views

urlpatterns = [
    path('directors/', views.director_list_api_view),
    path('movies/', views.movie_list_api_view),
    path('reviews/', views.review_list_api_view),
    path('directors/<int:id>/', views.director_detail_api_view),
    path('movies/<int:id>/', views.movie_detail_api_view),
    path('reviews/<int:id>/', views.review_detail_api_view),
    path('directors/', views.directors_list),
    path('movies/reviews/', views.movie_reviews),
    path('directors/', views.DirectorListCreate),
    path('directors/<int:pk>/', views.DirectorRetrieveUpdateDestroy),
    path('movies/', views.MovieListCreate),
    path('movies/<int:pk>/', views.MovieRetrieveUpdateDestroy),
    path('reviews/', views.ReviewListCreate),
    path('reviews/<int:pk>/', views.DirectorRetrieveUpdateDestroy),

]
