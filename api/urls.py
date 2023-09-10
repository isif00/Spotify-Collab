from django.urls import path
from .views import RoomView
from .views import CreateRoomView

urlpatterns = [
    path('rooms/', RoomView.as_view(), name='room-list'),
    path('create-room/', CreateRoomView.as_view(), name='create-room'),
]