from django.contrib import admin
from .models.category import Categor
from .models.products import Product
# Register your models here.
admin.site.register(Categor)
admin.site.register(Product)