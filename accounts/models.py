from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="default.jpg")
    description = models.TextField(max_length=200)

    def __str__(self):
        return f"{self.user.username}'s Profile"

   