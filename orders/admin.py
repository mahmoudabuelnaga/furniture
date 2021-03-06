from django.contrib import admin
from .models import Order, OrderItem
from import_export.admin import ImportExportModelAdmin


# Register your models here.
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']

@admin.register(Order)
class OrderAdmin(ImportExportModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city', 'created', 'updated', 'paid']
    list_filter = ['paid', 'created','updated']
    inlines = [OrderItemInline]