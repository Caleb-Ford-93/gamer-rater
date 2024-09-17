from django.db import models
from django.contrib.auth.models import User


class Game(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField(max_length=450)
    designer = models.CharField(max_length=255)
    year_released = models.IntegerField()
    number_of_players = models.IntegerField()
    est_time = models.FloatField()
    age_recommendation = models.IntegerField()
    categories = models.ManyToManyField(
        "Category", through="GameCategory", related_name="games"
    )
