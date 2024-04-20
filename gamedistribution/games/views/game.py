from rest_framework import status
from django.db.models import Q
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

from games.models import Game
from helper.search import SearchFilter
from games.serializers.game import GameSerializer

class GameListApiView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = GameSerializer
    queryset = Game.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        search_term = self.request.query_params.get('search', '')

        if search_term:
            queryset = queryset.filter(title__icontains=search_term)

        tags = self.request.query_params.getlist('tags')
        if tags:
            print(tags)
            tag_filter = Q(tags__id__in=tags)
            queryset = queryset.filter(tag_filter)

        developers = self.request.query_params.getlist('developers')
        if developers:
            developer_filter = Q(developers__id__in=developers)
            queryset = queryset.filter(developer_filter)

        genres = self.request.query_params.getlist('genres')
        if genres:
            genre_filter = Q(genres__id__in=genres)
            queryset = queryset.filter(genre_filter)
        print(queryset)
        return queryset

class GameRetrieveApiView(RetrieveAPIView):
    permission_classes = [AllowAny]
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class GameCreateAPIView(CreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class GameRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = Game.objects.all()
    serializer_class = GameSerializer