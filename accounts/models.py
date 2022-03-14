from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="default.jpg")
    description = models.TextField(max_length=200)

    def __str__(self):
        return f"{self.user.username}'s Profile"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.name)

        if img.width > 300 or img.height > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.name)