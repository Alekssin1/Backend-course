from games.views.base import ListView, RetrieveView, CreateView, RetrieveUpdateDestroyView
from games.models import Tag
from games.serializers.tag import TagSerializer


class TagListApiView(ListView):
    queryset = Tag.objects.prefetch_related('games')
    serializer_class = TagSerializer

class TagRetrieveApiView(RetrieveView):
    queryset = Tag.objects.prefetch_related('games')
    serializer_class = TagSerializer

class TagCreateAPIView(CreateView):
    queryset = Tag.objects.prefetch_related('games')
    serializer_class = TagSerializer

class TagRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyView):
    queryset = Tag.objects.prefetch_related('games')
    serializer_class = TagSerializer
