from django.urls import path
from .views import RoomView

urlpatterns = [
    path('home/', RoomView.as_view()),
    path('create-room', RoomView.as_view()),
]