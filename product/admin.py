from django.contrib import admin
from .models import Category
from .models import Product
from .models import TypeCar
from .models import Services


# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(TypeCar)
admin.site.register(Services)
