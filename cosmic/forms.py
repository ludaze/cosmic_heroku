from django import forms
from .models import *

class CustomerForm(forms.ModelForm):
    
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'phone_number form-control' }))
    customer_address = forms.CharField(widget=forms.TextInput(attrs={'class': 'customer_address form-control'}))

    customer_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter name'}),
    )
    email = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter e-mail'}),
    )
    
    class Meta:
   
        model = cosmic_customer_profile
        fields = ['customer_name','customer_address','email','phone_number','contact_person','comments']

class SupplierForm(forms.ModelForm):
    
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'phone_number form-control' }))
    supplier_address = forms.CharField(widget=forms.TextInput(attrs={'class': 'customer_address form-control'}))

    supplier_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter name'}),
    )
    email = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter e-mail'}),
    )
    
    class Meta:
   
        model = cosmic_supplier_profile
        fields = ['supplier_name','supplier_address','email','phone_number','contact_person','comments']

class CosmicOrderForm(forms.ModelForm):
    
     order_no = forms.CharField(widget=forms.TextInput(attrs={'class': 'order_no form-control'}))

    class Meta:
   
        model = cosmic_order
        fields = ['customer_name','total_price','order_no','date','payment_type','measurement_type','approved_by','PR_before_vat','transportation','shipment_type']

class OrderItemForm(forms.ModelForm):
   
    before_vat = forms.DecimalField(
        label='Total Price',
        required=False,
        widget=forms.TextInput(attrs={'class': 'before_vat form-control', 'readonly': 'readonly'})
    )
    measurement = forms.CharField(widget=forms.TextInput(attrs={'class': 'measurement form-control'}), required=False)
    quantity = forms.FloatField(widget=forms.TextInput(attrs={'class': 'quantity form-control' }))
    price = forms.DecimalField(widget=forms.TextInput(attrs={'class': 'price form-control'}))

    item_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter name'}),
    )
    hs_code = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'HS-CODE'}),
    )
    
    class Meta:
   
        model = order_item
        fields = ['total_price', 'item_name','hs_code','price','quantity','before_vat','measurement']

class CosmicPurchaseForm(forms.ModelForm):
    
    purchase_no = forms.CharField(widget=forms.TextInput(attrs={'class': 'purchase_no form-control'}))

    class Meta:
   
        model = cosmic_purchase
        fields = ['supplier_name','total_price','purchase_no','date','payment_type','measurement_type','before_vat','transportation','shipment_type']

class ShippingForm(forms.ModelForm):
    
    class Meta:
   
        model = shipping_info
        fields = ['freight_amount','invoice_date','port_of_loading','port_of_discharge','final_destination','container_no','truck_waybill_no','country_of_origin']
