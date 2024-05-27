from django.urls import path
from .views import RoomView

#if you get a url that is blank return the main function
urlpatterns = [
    path('home',RoomView.as_view()),
]