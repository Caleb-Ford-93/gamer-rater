from django.db import models
from django.contrib.auth.models import User


class GamePicture(models.Model):
    game = models.ForeignKey("Game", on_delete=models.CASCADE, related_name="picture")
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_pictures"
    )
    image = models.ImageField(
        upload_to=None, height_field=None, width_field=None, max_length=100
    )
