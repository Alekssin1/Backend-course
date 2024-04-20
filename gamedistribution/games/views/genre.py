from rest_framework import status
from rest_framework.generics import (
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
    RetrieveUpdateAPIView,
    ListCreateAPIView,
    CreateAPIView,
    DestroyAPIView,
    RetrieveAPIView
)
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response

from games.models import Genre
from games.serializers.genre import GenreSerializer


class GenreListApiView(ListAPIView):
    permission_classes = [AllowAny]
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class GenreRetrieveApiView(RetrieveAPIView):
    permission_classes = [AllowAny]
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class GenreCreateAPIView(CreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [IsAdminUser]
    

class GenreRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer