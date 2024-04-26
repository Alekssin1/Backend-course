from django.core.management.base import BaseCommand
from user.models import User
from games.models import Genre, Developer, Tag, Game, Review
from faker import Faker
import os
import random

fake = Faker()

class Command(BaseCommand):
    help = 'Seed the database with fake games'
    
    def handle(self, *args, **kwargs):
        self.stdout.write("Seeding the database with fake games..")

        # Predefined list of genres
        genres = ['Action', 'Adventure', 'Role-Playing', 'Strategy', 'Simulation', 'Sports', 'Puzzle', 'Racing', 'Fighting', 'Horror']

        # Insert genres into the database
        for genre_name in genres:
            Genre.objects.get_or_create(name=genre_name)

        # Generate developers
        for _ in range(10):
            Developer.objects.create(name=fake.company())

        # Generate tags
        for _ in range(10):
            Tag.objects.create(name=fake.word())

        image_directory = 'games/management/images'
        
        # Create a dictionary to keep track of how many times each image has been used
        image_usage_count = {image_filename: 0 for image_filename in os.listdir(image_directory)}

        # Generate games
        for _ in range(30):
            image_filename = min(image_usage_count, key=image_usage_count.get)
            image_usage_count[image_filename] += 1
            game = Game(
                title=' '.join(fake.words(nb=random.randint(1, 4))),
                price=fake.pydecimal(left_digits=2, right_digits=2, positive=True),
                description=fake.text()
            )

            # Set discount price randomly for some games
            if random.choice([True, False]):
                game.discount_price = fake.pydecimal(left_digits=2, right_digits=2, positive=True, max_value=game.price)

            game.save()

            # Add random developers and tags to the game
            game.developers.set(Developer.objects.order_by('?')[:2])
            game.tags.set(Tag.objects.order_by('?')[:2])

            # Add predefined genres to the game
            random_num_genres = random.randint(1, 4)
            random_genres = random.sample(genres, k=random_num_genres)
            for genre_name in random_genres:
                genre, _ = Genre.objects.get_or_create(name=genre_name)
                game.genres.add(genre)

            users = User.objects.order_by('?')[:random.randint(2, 7)]

            # Generate reviews for the game
            for user in users:
                Review.objects.create(
                    game=game,
                    user=user,
                    comment=fake.paragraph()
                )

            # Assign random image to the game
            image_path = os.path.join(image_directory, image_filename)
            game.image.save(image_filename, open(image_path, 'rb'), save=True)

        self.stdout.write(self.style.SUCCESS("Fake data for games seeding completed successfully!"))
