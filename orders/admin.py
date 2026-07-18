from django.contrib import admin
from .models import Address, Cart, CartItem, Order, OrderItem

admin.site.register(Address)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(OrderItem)