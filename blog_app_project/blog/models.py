from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Classes here are database tables
# Django uses SQLite for it and whenever a Django project is created, db.sqlite3 file is automatically generated
class Post(models.Model):

    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
