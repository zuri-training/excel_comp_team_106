from django.db import models
from django.contrib.auth.models import User

from PIL import Image
import os
from django.conf import settings

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    site = os.path.join(settings.MEDIA_ROOT, 'profile_images')
    avatar = models.ImageField(default='default.jpg', upload_to= site)
    bio = models.TextField()

    def __str__(self):
        return self.user.username
    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.avatar.path)

        if img.height > 120 or img.width > 70:
            new_img = (120, 70)
            img.thumbnail(new_img)
            img.save(self.avatar.path)