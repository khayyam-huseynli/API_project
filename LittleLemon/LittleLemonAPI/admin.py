from django.contrib import admin
from . models import MenuItem, Category, Cart, OrderItem, Order

admin.site.register(MenuItem)
admin.site.register(Category)
admin.site.register(Cart)
admin.site.register(OrderItem)
admin.site.register(Order)



