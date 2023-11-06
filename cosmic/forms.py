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
