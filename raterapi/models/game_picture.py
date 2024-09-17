from django.db import models
from django.contrib.auth.models import User


class Game_Picture(models.Model):
    game = models.ForeignKey("Games", on_delete=models.CASCADE, related_name="pictures")
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_pictures"
    )
    image = models.ImageField(
        upload_to=None, height_field=None, width_field=None, max_length=100
    )
