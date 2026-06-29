from django.db import models

class Dealer(models.Model):
    name = models.CharField(max_length=100)
    adress = models.TextField(max_length=500)

    class Meta:
        db_table = 'dealer'

class Car(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    description = models.TextField()
    photo = models.ImageField(upload_to='cars/')
    owner_website = models.URLField(null=True, blank=True)
    is_available = models.BooleanField(default=True)
    dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.brand} {self.model}"
    
    class Meta:
        db_table = 'cars'


