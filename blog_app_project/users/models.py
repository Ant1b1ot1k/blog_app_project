from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    # Establishing 1:1 relation with User model and existing project model
    user = models.OneToOneField(User, on_delete=models.CASCADE) # If user is deleted, delete profile but if profile is deleted, user is not deleted
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
