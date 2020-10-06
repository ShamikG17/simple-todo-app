from django.db import models
from django.utils import timezone

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=60)
    text = models.CharField(max_length=300)
    create_date = models.DateTimeField(default=timezone.now())
    completed = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return self.title

