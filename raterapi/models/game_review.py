from django.contrib.auth.models import User
from django.db import models


class GameReviews(models.Model):
    game = models.ForeignKey("Game", on_delete=models.CASCADE, related_name="games")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    content = models.CharField(max_length=600)
