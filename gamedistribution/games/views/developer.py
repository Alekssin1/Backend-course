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

from games.models import Developer
from games.serializers.developer import DeveloperSerializer


class DeveloperListApiView(ListAPIView):
    permission_classes = [AllowAny]
    queryset = Developer.objects.all()
    serializer_class = DeveloperSerializer


class DeveloperRetrieveApiView(RetrieveAPIView):
    permission_classes = [AllowAny]
    queryset = Developer.objects.all()
    serializer_class = DeveloperSerializer


class DeveloperCreateAPIView(CreateAPIView):
    queryset = Developer.objects.all()
    serializer_class = DeveloperSerializer
    permission_classes = [IsAdminUser]
    

class DeveloperRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = Developer.objects.all()
    serializer_class = DeveloperSerializer