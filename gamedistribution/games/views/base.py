from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    RetrieveUpdateDestroyAPIView,
    GenericAPIView
)
from rest_framework.permissions import AllowAny, IsAdminUser

class BaseAPIView(GenericAPIView):
    permission_classes = [AllowAny]
    queryset = None
    serializer_class = None


class ListView(BaseAPIView, ListAPIView):
    pass

class RetrieveView(BaseAPIView, RetrieveAPIView):
    pass

class CreateView(BaseAPIView, CreateAPIView):
    permission_classes = [IsAdminUser]

class RetrieveUpdateDestroyView(BaseAPIView, RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
