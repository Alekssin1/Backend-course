import os
from games.models import Tag, Genre, Developer, Game
from games.services.image_converter import ImageService

class GameService:
    @staticmethod
    def _get_or_create_objects(names, model):
        return [model.objects.get_or_create(name=name)[0] for name in names]

    @staticmethod
    def create_game(validated_data, tag_names, genre_names, developer_names):
        tags = GameService._get_or_create_objects(tag_names, Tag)
        genres = GameService._get_or_create_objects(genre_names, Genre)
        developers = GameService._get_or_create_objects(developer_names, Developer)

        game = Game.objects.create(**validated_data)
        game.tags.set(tags)
        game.genres.set(genres)
        game.developers.set(developers)

        return game

    @staticmethod
    def update_game(instance, validated_data, tag_names, genre_names, developer_names, new_image):
        previous_image_url = instance.image.url if instance.image else None
        print(previous_image_url)
        for key, value in validated_data.items():
            setattr(instance, key, value)

        if new_image:
            new_image_path = instance.image.path
            ImageService.convert_and_resize_image(new_image, new_image_path)

            # instance.image.name = new_image.name
            # print(new_image.name)


        if tag_names and tag_names!=[""]:
            tags = GameService._get_or_create_objects(tag_names, Tag)
            instance.tags.set(tags)
        if genre_names and genre_names!=[""]:
            genres = GameService._get_or_create_objects(genre_names, Genre)
            instance.genres.set(genres)
        if developer_names and developer_names!=[""]:
            developers = GameService._get_or_create_objects(developer_names, Developer)
            instance.developers.set(developers)

        

        return instance