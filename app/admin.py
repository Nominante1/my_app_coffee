from django.contrib import admin
from .models import Supplier, Coffee, Product_Storage

admin.site.register(Supplier)
admin.site.register(Coffee)
admin.site.register(Product_Storage)