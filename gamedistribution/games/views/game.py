from django.db.models import Q
from games.views.base import ListView, RetrieveView, CreateView, RetrieveUpdateDestroyView
from games.models import Game
from games.serializers.game import GameSerializer

class GameListApiView(ListView):
    serializer_class = GameSerializer
    queryset = Game.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        search_term = self.request.query_params.get('search', '')
        tags = self.request.query_params.getlist('tags')
        developers = self.request.query_params.getlist('developers')
        genres = self.request.query_params.getlist('genres')

        filters = Q()

        if search_term:
            filters &= Q(title__icontains=search_term)
        
        if tags:
            filters &= Q(tags__id__in=tags)

        if developers:
            filters &= Q(developers__id__in=developers)

        if genres:
            filters &= Q(genres__id__in=genres)

        queryset = queryset.filter(filters)

        return queryset

class GameRetrieveApiView(RetrieveView):
    queryset = Game.objects.all().prefetch_related('reviews', 'tags', 'developers', 'genres')
    serializer_class = GameSerializer

class GameCreateAPIView(CreateView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class GameRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyView):
    queryset = Game.objects.all().prefetch_related('reviews', 'tags', 'developers', 'genres')
    serializer_class = GameSerializer