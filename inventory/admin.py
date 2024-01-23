from django.contrib import admin
from inventory.models import Product, Inventory, ProductInventory

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    fields = ["name", "price", "units_measurement", "amount"]

@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ["id", "date"]
    fields = ["date"]

@admin.register(ProductInventory)
class ProductInventoryAdmin(admin.ModelAdmin):
    list_display = ["id", "product", "inventory"]
    fields = ["product", "inventory", "amount"]