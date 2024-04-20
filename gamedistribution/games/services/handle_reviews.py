from games.models import Review

class ReviewService:
    @staticmethod
    def get_user_reviews(user, game_id):
        return Review.objects.filter(user=user, game_id=game_id)

    @staticmethod
    def can_update_review(review, user):
        return review.user == user

    @staticmethod
    def can_delete_review(review, user):
        return review.user == user or user.is_staff