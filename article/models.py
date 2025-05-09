from django.db import models

class Sneaker(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='sneakers/')

    def __str__(self):
        return self.name
