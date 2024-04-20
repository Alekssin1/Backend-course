from games.views.base import ListView, RetrieveView, CreateView, RetrieveUpdateDestroyView
from games.models import Developer
from games.serializers.developer import DeveloperSerializer


class DeveloperListApiView(ListView):
    queryset = Developer.objects.prefetch_related('games')
    serializer_class = DeveloperSerializer

class DeveloperRetrieveApiView(RetrieveView):
    queryset = Developer.objects.prefetch_related('games')
    serializer_class = DeveloperSerializer

class DeveloperCreateAPIView(CreateView):
    queryset = Developer.objects.prefetch_related('games')
    serializer_class = DeveloperSerializer

class DeveloperRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyView):
    queryset = Developer.objects.prefetch_related('games')
    serializer_class = DeveloperSerializer