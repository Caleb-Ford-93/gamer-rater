from django.db import models
from django.contrib.auth.models import User


class GameRating(models.Model):
    game = models.ForeignKey("Game", on_delete=models.CASCADE, related_name="rating")
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_ratings"
    )
    rating = models.IntegerField()
