from django.db import models

# Create your models here.

class Note(models.Model):
    title = models.CharField()
    content = models.TextField()

    def __str__(self):
        return f"{self.title}"