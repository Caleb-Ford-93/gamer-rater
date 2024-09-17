from django.contrib.auth.models import User
from django.db import models


class GameReview(models.Model):
    game = models.ForeignKey("Game", on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_reviews"
    )
    content = models.CharField(max_length=600)
