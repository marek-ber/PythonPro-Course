from django.db import models

# Create your models here.

class Ogloszenia(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    created_add = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"
    
    class Meta:
        db_table = 'ogloszenia'