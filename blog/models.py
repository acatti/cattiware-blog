from django.db import models
from django.utils import timezone

class Post(models.Model):   #definizione modello. "models.Model" -> salva Post nel DBase
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=32)
    subtitle = models.CharField(max_length=64)
    text = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    
    def __str__(self):
        return self.title