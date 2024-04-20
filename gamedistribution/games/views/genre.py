from games.views.base import ListView, RetrieveView, CreateView, RetrieveUpdateDestroyView
from games.models import Genre
from games.serializers.genre import GenreSerializer

class GenreListApiView(ListView):
    queryset = Genre.objects.prefetch_related('games')
    serializer_class = GenreSerializer

class GenreRetrieveApiView(RetrieveView):
    queryset = Genre.objects.prefetch_related('games')
    serializer_class = GenreSerializer

class GenreCreateAPIView(CreateView):
    queryset = Genre.objects.prefetch_related('games')
    serializer_class = GenreSerializer

class GenreRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyView):
    queryset = Genre.objects.prefetch_related('games')
    serializer_class = GenreSerializer

