from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    """Класс,отображаения заказанных продуктов"""
    model = OrderItem


class OrderAdmin(admin.ModelAdmin):
    """Класс отображаения информации по заказу"""
    list_display = ['id','first_name', 'last_name', 'email',
                    'address', 'postal_code', 'city', 'paid',
                    'created', 'updated']
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]

admin.site.register(Order, OrderAdmin)