from random import choice
from django.shortcuts import render, get_object_or_404
from django.db.models import Min

from mailing.forms import SubscribeForm
from .models import Game, Genre

def app_render(request):
    return render(request, "contact.html")

def shop(request):
    games = Game.objects.all()

    genre_filter = request.GET.get('genre')
    if genre_filter:
        games = games.filter(genres__name=genre_filter)

    genres = Genre.objects.all()

    context = {
        'games': games,
        'genres': genres,
        'selected_genre': genre_filter
    }

    return render(request, 'shop.html', context)


def product(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    return render(request, "product-details.html", {'game': game})

def search_view(request):
    if request.method == 'POST':
        search_keyword = request.POST.get('searchKeyword')
        if search_keyword:
            results = Game.objects.filter(title__icontains=search_keyword)
        else:
            results = None
        return render(request, 'search.html', {'results': results})
    return render(request, 'search.html', {'results': None})

def home(request):
    genres_with_random_games = Genre.objects.annotate(
        random_game_image=Min('games__image')
    ).values('name', 'random_game_image')

    random_discount_game = Game.objects.filter(discount_price__isnull=False).order_by('?').first()
    discount_percentage = 100 * (random_discount_game.price - random_discount_game.discount_price) / random_discount_game.price

    most_popular_games = Game.objects.order_by('-downloads')[:4]

    latest_games = Game.objects.order_by('-id')[:4]
    form = SubscribeForm()
    context = {
        'random_game': random_discount_game,
        'discount_percentage': discount_percentage,
        'genres_with_random_games': genres_with_random_games,
        'most_popular_games': most_popular_games,
        'latest_games': latest_games,
        'form':form,
    }
    return render(request, "index.html", context)