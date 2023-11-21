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
    path('display_purchase', views.display_purchase, name='display_purchase'),
    path('display_supplier_profile', views.display_supplier_profile, name='display_supplier_profile'),
    path('create_order', views.create_order, name='create_order'),
    path('create_shipping', views.create_shipping, name='create_shipping'),
    
]
