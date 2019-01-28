from django.db import models
from django.utils import timezone
import datetime

class Category(models.Model):
    name = models.CharField(max_length = 200)
    creation_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name


class Task(models.Model):
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    summary = models.CharField(max_length = 200)
    pubDate = models.DateTimeField(auto_now_add=True)
    updatedTime = models.DateTimeField(auto_now=True)
    description = models.CharField(max_length = 500)
    startDate = models.DateField(blank = True, null = True)
    endDate = models.DateField(blank = True, null = True)
    isDone = models.BooleanField(default=False)
    def wasPublishedRecently(self):
        return self.pubDate >= timezone.now() - datetime.timedelta(days = 1)

    def __str__(self):
        return self.summary

