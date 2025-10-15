from django.contrib import admin
from .models import Category, MenuItem, Topping, Order, OrderItem, OrderItemTopping

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'order']
    list_editable = ['order']

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'tag', 'order']
    list_filter = ['category', 'tag']
    list_editable = ['order']
    search_fields = ['name', 'description']

@admin.register(Topping)
class ToppingAdmin(admin.ModelAdmin):
    list_display = ['name', 'topping_type', 'calories', 'is_available']
    list_filter = ['topping_type', 'is_available']
    list_editable = ['is_available']

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer_name', 'order_type', 'status', 'total', 'created_at']
    list_filter = ['status', 'order_type', 'created_at']
    search_fields = ['customer_name', 'customer_email', 'customer_phone']
    inlines = [OrderItemInline]

admin.site.register(OrderItemTopping)

