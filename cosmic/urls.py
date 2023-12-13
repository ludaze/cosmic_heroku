from django.contrib import admin
from django.urls import path, include
from cosmic import views

urlpatterns = [

    path('create_customer', views.create_customer, name='create_customer'),
    path('create_supplier', views.create_supplier, name='create_supplier'),
    path('display_customer', views.display_customer, name='display_customer'),
    path('display_customer_profile', views.display_customer_profile, name='display_customer_profile'),
    path('display_supplier', views.display_supplier, name='display_supplier'),
    path('display_order', views.display_order, name='display_order'),
    path('display_supplier_profile', views.display_supplier_profile, name='display_supplier_profile'),
    path('create_order', views.create_order, name='create_order'),
    path('create_shipping', views.create_shipping, name='create_shipping'),
    path('order_approval', views.order_approval, name='order_approval'),
    path('order_status', views.order_status, name='order_status'),
    path('edit_order', views.edit_order, name='edit_order'),
    path('commercial_invoice', views.commercial_invoice, name='commercial_invoice'),
    path('print_order', views.print_order, name='print_order'),
    path('bill_of_lading', views.bill_of_lading, name='bill_of_lading'),
    path('packing_list', views.packing_list, name='packing_list'),
]
