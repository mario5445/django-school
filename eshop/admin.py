from django.contrib import admin
from . models import *

# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Customer)
# admin.site.register(Order_detail)
# admin.site.register(Order_product)
admin.site.register(Order)