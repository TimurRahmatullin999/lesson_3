from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname')

@admin.register(models.Storage)
class StorageAdmin(admin.ModelAdmin):
    list_display = ('street', 'number_of_street')

@admin.register(models.Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname')

@admin.register(models.Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('title', 'price')

@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('offered_price',)

@admin.register(models.HistoryOrder)
class HistoryOrderAdmin(admin.ModelAdmin):
    list_display = ('date_make_order',)
