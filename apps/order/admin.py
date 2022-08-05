from django.contrib import admin
from apps.order.models import Category, FoodItem, Menu, Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    fields = ('food', 'order', 'quantity', 'unit_price')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'order_date', 'order_items_quantity')
    list_display_links = ('id', 'customer')
    fields = ('customer', 'order_date', 'pickup_date')
    readonly_fields = ('order_date',)
    inlines = [OrderItemInline]


class FoodItemInline(admin.TabularInline):
    model = FoodItem
    fields = ('name', 'category', 'quantity', 'unit_price')

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'restaurant', 'created_at')
    list_display_links = ('id', 'restaurant')
    inlines = [FoodItemInline]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

