from django.db import models
from django.contrib.auth.models import User

class Item(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=3)
    image = models.ImageField(null=True, blank=True)
    quantity=models.IntegerField(default=1)

    
class Cart(models.Model):
	item = models.ForeignKey(Item, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	price = models.DecimalField(max_digits=10, decimal_places=3)
	quantity = models.IntegerField(default=1)