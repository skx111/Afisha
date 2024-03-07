from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register),
    path('confirm/', views.login_view),
]

