from django.urls import path
from .views.tag import TagRetrieveApiView, TagListApiView, TagCreateAPIView, TagRetrieveUpdateDestroyAPIView
from .views.genre import GenreRetrieveApiView, GenreListApiView, GenreCreateAPIView, GenreRetrieveUpdateDestroyAPIView
from .views.developer import DeveloperRetrieveApiView, DeveloperListApiView, DeveloperCreateAPIView, DeveloperRetrieveUpdateDestroyAPIView
from .views.game import GameListApiView, GameRetrieveApiView, GameCreateAPIView, GameRetrieveUpdateDestroyAPIView
from .views.review import ReviewListCreateAPIView, ReviewRetrieveUpdateDestroyAPIView

urlpatterns = [
    path("tags/", TagListApiView.as_view(), name="all_tags"),
    path("tags/<pk>/", TagRetrieveApiView.as_view(), name="one_tag"),
    path('tags/admin/create/', TagCreateAPIView.as_view(), name='admin_tag_create'),
    path('tags/admin/<pk>/', TagRetrieveUpdateDestroyAPIView.as_view(), name='admin_tag'),

    path("genres/", GenreListApiView.as_view(), name="all_genres"),
    path("genres/<pk>/", GenreRetrieveApiView.as_view(), name="one_genre"),
    path('genres/admin/create/', GenreCreateAPIView.as_view(), name='admin_genre_create'),
    path('genres/admin/<pk>/', GenreRetrieveUpdateDestroyAPIView.as_view(), name='admin_genre'),

    path("developers/", DeveloperListApiView.as_view(), name="all_developers"),
    path("developers/<pk>/", DeveloperRetrieveApiView.as_view(), name="one_developer"),
    path('developers/admin/create/', DeveloperCreateAPIView.as_view(), name='admin_developer_create'),
    path('developers/admin/<pk>/', DeveloperRetrieveUpdateDestroyAPIView.as_view(), name='admin_developer'),
    
    path("games/", GameListApiView.as_view(), name="all_games"),
    path("games/<pk>/", GameRetrieveApiView.as_view(), name="one_game"),
    path("games/admin/create/", GameCreateAPIView.as_view(), name="admin_game_create"),
    path("games/admin/<pk>/", GameRetrieveUpdateDestroyAPIView.as_view(), name="admin_game"),

    path("reviews/", ReviewListCreateAPIView.as_view(), name="all_reviews"),
    path("reviews/<pk>/", ReviewRetrieveUpdateDestroyAPIView.as_view(), name="one_review"),
]
