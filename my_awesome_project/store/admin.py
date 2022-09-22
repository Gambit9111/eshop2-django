from django.contrib import admin
from .models import Category, Product, Order, OrderItem

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'active')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('uuid' ,'device', 'completed', 'paid', 'delivered', 'date_ordered', 'get_cart_total')
    list_filter = (
        ('items', admin.RelatedOnlyFieldListFilter),
    )
@admin.register(OrderItem)
# display order items filtered by order
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order' ,'product', 'quantity', 'get_total', 'date_added')
    list_filter = (
        ('order', admin.RelatedOnlyFieldListFilter),
    )
