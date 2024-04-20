from rest_framework import serializers
from django.conf import settings

from games.models import Game
from games.services.handle_games import GameService


class GameSerializer(serializers.ModelSerializer):
    from games.serializers.genre import GenreSerializer
    from games.serializers.tag import TagSerializer
    from games.serializers.developer import DeveloperSerializer
    from games.serializers.review import ReviewSerializer  

    image = serializers.SerializerMethodField()
    genres = GenreSerializer(many=True, required=False)
    tags = TagSerializer(many=True, required=False)
    developers = DeveloperSerializer(many=True, required=False)
    reviews = ReviewSerializer(many=True, read_only=True)  

    def get_image(self, instance):
        if instance.image:
            return f"{settings.HOST}:{settings.PORT}{instance.image.url}"

    class Meta:
        model = Game
        fields = ("id", "title", "image", "price", "discount_price",
                  "description", "developers", "genres", "tags", "downloads", "reviews")
        
    def create(self, validated_data):
        tag_names = self.context['request'].data.get('tag_names', "").split(",")
        genre_names = self.context['request'].data.get('genre_names', "").split(",")
        developer_names = self.context['request'].data.get('developer_names', "").split(",")
        image = self.context['request'].data.get('image', None)
        game_data = {key: value for key, value in validated_data.items() if key not in ['tag_names', 'genre_names', 'developer_names']}
        game_data['image'] = image

        game = GameService.create_game(game_data, tag_names, genre_names, developer_names)

        return game
    
    def update(self, instance, validated_data):
        tag_names = self.context['request'].data.get('tag_names', "").split(",")
        genre_names = self.context['request'].data.get('genre_names', "").split(",")
        developer_names = self.context['request'].data.get('developer_names', "").split(",")
        image = self.context['request'].data.get('image', None)
        return GameService.update_game(instance, validated_data, tag_names, genre_names, developer_names, image)