from django.contrib import admin
from .models import addProduct, saleProduct, add_Purchase, add_Member

# Register your models here.
admin.site.register(addProduct)
admin.site.register(saleProduct)
admin.site.register(add_Purchase)
admin.site.register(add_Member)