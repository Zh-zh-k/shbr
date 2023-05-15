from django.contrib import admin
from .models import Couriers, Orders

@admin.register(Couriers)
class CouriersAdmin(admin.ModelAdmin):
    list_display = ['id', 'courier_type', 'regions', 'working_hours', 'orders']
    search_fields = ['courier_type', 'regions', 'working_hours', 'orders']
    list_editable = ['courier_type', 'regions', 'working_hours']
    list_filter = ['courier_type', 'regions', 'working_hours', 'orders']

@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ['id', 'weight', 'regions', 'cost', 'complete_time', 'courier']
    search_fields = ['weight', 'regions', 'cost', 'complete_time', 'courier']
    list_editable = ['weight', 'regions', 'cost', 'complete_time', 'courier']
    list_filter = ['weight', 'regions', 'cost', 'complete_time', 'courier']
