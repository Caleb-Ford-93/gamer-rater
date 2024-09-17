from django.db import models


class Game_Categories(models.Model):
    game = models.ForeignKey("Games", on_delete=models.CASCADE, related_name="games")
    category = models.ForeignKey(
        "Categories", on_delete=models.CASCADE, related_name="categories"
    )
