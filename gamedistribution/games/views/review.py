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
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from games.models import Review
from games.serializers.review import ReviewSerializer
from games.services.handle_reviews import ReviewService


class ReviewListCreateAPIView(ListCreateAPIView):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        user_reviews = ReviewService.get_user_reviews(request.user, request.data.get('game'))
        if user_reviews.exists():
            return Response({"error": "You have already reviewed this game"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        return Response(serializer.data)

class ReviewRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if not ReviewService.can_update_review(instance, request.user):
            return Response({"error": "You are not allowed to update this review"}, status=status.HTTP_403_FORBIDDEN)
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if not ReviewService.can_delete_review(instance, request.user):
            return Response({"error": "You are not allowed to delete this review"}, status=status.HTTP_403_FORBIDDEN)
        self.perform_destroy(instance)
        return Response({"message": "Object successfully deleted."}, status=status.HTTP_200_OK)