from django.db import models
from django.contrib.auth.models import User


class GameRating(models.Model):
    game = models.ForeignKey("Games", on_delete=models.CASCADE, related_name="game")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    rating = models.IntegerField()
