from django.db import models
from .category import Categor

class Product(models.Model):
    name = models.CharField(max_length=60)
    narxi = models.IntegerField(default=0)
    rasmi = models.ImageField()
    category = models.ForeignKey(Categor, on_delete=models.CASCADE, default = 1)
    def __str__(self):
        return self.name

