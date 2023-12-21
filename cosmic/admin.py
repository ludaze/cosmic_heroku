from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import cosmic_order,cosmic_purchase,order_item,customer_profile,supplier_profile
# Register your models here.
admin.site.register(cosmic_order)
admin.site.register(cosmic_purchase)
admin.site.register(order_item)
admin.site.register(customer_profile)
admin.site.register(supplier_profile)