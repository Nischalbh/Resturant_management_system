from django.contrib import admin
from .models import *


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


class FoodAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "category")
    search_fields = ("name",)
    list_filter = ("category",)


class TableAdmin(admin.ModelAdmin):
    list_display = ("id", "number", "capacity", "is_available")
    search_fields = ("number",)
    list_filter = ("is_available",)


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    autocomplete_fields = ("food",)
    extra = 1


class OrderAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "quantity", "total_price", "Status", "payment_status"]
    search_fields = ["user__username"]
    list_filter = ["Status", "payment_status"]
    inlines = [
        OrderItemInline,
    ]


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ["id", "order", "food"]
    search_fields = [
        "food_name",
        "order__user__username",
    ]
    list_filter = [
        "food",
    ]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Food, FoodAdmin)
admin.site.register(Table, TableAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
