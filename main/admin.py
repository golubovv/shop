from django.contrib import admin
from .models import *


class Buyers_Admin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'numbersTel', 'shopping_cart')
    list_display_links = ('first_name', 'last_name')
    search_fields = ('first_name', 'last_name', 'numbersTel')


class Orders_Admin(admin.ModelAdmin):
    list_display = ('orders_buy', 'order_numb', 'order_date', 'status_order')
    search_fields = ('orders_buy', 'order_date', 'order_numb')
    list_editable = ('status_order',)
    list_display_links = ('orders_buy', 'order_numb')


class Goods_Admin(admin.ModelAdmin):
    list_display = ('goods_name', 'brend', 'shop_price', 'count_goods')
    list_display_links = ('goods_name',)
    search_fields = ('goods_name', 'brend')
    list_editable = ('shop_price',)
    list_filter = ('goods_name', 'brend')


class PropertyGoods_Admin(admin.ModelAdmin):
    list_display = ('nameProperty', 'unitProperty', 'quantyProperty', 'boolProperty', 'boolValueProperty')
    list_display_links = ('nameProperty',)
    search_fields = ('nameProperty',)
    list_editable = ('quantyProperty', 'boolProperty', 'boolValueProperty',)

admin.site.register(Goods, Goods_Admin)
admin.site.register(Orders, Orders_Admin)
admin.site.register(Buyers, Buyers_Admin)
admin.site.register(PropertyGoods, PropertyGoods_Admin)
admin.site.register(Categories)
admin.site.register(Makers)

# Register your models here.
