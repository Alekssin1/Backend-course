from django.shortcuts import get_object_or_404
from games.models import Game, Genre
from django.db.models import Min

class DBQueryManager:
    @staticmethod
    def get_all_games():
        return Game.objects.all()

    @staticmethod
    def get_games_by_genre(genre_filter):
        return Game.objects.filter(genres__name=genre_filter)

    @staticmethod
    def get_all_genres():
        return Genre.objects.all()

    @staticmethod
    def get_game_by_id(game_id):
        return get_object_or_404(Game, pk=game_id)

    @staticmethod
    def search_games_by_keyword(keyword):
        if keyword:
            return Game.objects.filter(title__icontains=keyword)
        return None

    @staticmethod
    def get_random_discount_game():
        return Game.objects.filter(discount_price__isnull=False).order_by('?').first()

    @staticmethod
    def get_most_popular_games():
        return Game.objects.order_by('-downloads')[:4]

    @staticmethod
    def get_latest_games():
        return Game.objects.order_by('-id')[:4]

    @staticmethod
    def get_genres_with_random_games():
        return Genre.objects.annotate(
            random_game_image=Min('games__image')
        ).values('name', 'random_game_image')