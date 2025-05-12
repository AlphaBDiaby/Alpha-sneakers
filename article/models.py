from django.db import models

from sneakers.settings import AUTH_USER_MODEL


class Sneaker(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=128)
    brand = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='products/', blank=True, null=True)

    def __str__(self):
        return self.name



# Article (order)
"""
- Utilisateur
- Produit
- Quantité
- Commandé ou non
"""

class Order(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Sneaker, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.product.name} ({self.quantity})"



# panier(Cart)
"""
- Utilisateur
- Articles
- Commandé ou non
- Date de la commande
"""

class Cart(models.Model):
    user = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE)
    orders = models.ManyToManyField(Order)
    ordered = models.BooleanField(default=False)
    ordered_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.user.username