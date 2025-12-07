from django.contrib import admin
from .models import Shipment


@admin.register(Shipment)
class ShipmentAdmin(admin.ModelAdmin):
    list_display = ['tracking_number', 'order_number', 'carrier', 'status', 'created_at']
    list_filter = ['status', 'carrier', 'created_at']
    search_fields = ['tracking_number', 'order_number']
    readonly_fields = ['created_at', 'updated_at']
