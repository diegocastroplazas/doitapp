from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    biography = models.TextField(blank=True)
    picture = models.ImageField(upload_to = 'users/pictures', blank = True, null = True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

# Create your models here.
