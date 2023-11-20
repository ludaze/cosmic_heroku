from django.shortcuts import render
from django.shortcuts import render, redirect,get_object_or_404
from django.conf import settings
from .forms import *
from .models import *
from django.forms import formset_factory
from django.db.models import Sum
from django.http import JsonResponse,HttpResponse
from django.template.loader import get_template
import os
# Create your views here.
def create_customer(request):
    
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.errors:
            print(form.errors)
        if form.is_valid():
            try:
                form.save()
            except Exception as e:
                print(f"Error: {e}")
            return redirect('create_customer')
    
    else:
        
        form = CustomerForm()
    return render(request, 'create_customer.html', {'form': form })

def display_customer(request):
    if request.method == 'GET':
        customers = cosmic_customer_profile.objects.all()
        context = {
                    'my_customer': customers,
                }
          
        return render(request, 'display_customer.html', context)

def display_customer_profile(request):
    if request.method == 'GET':
        name = request.GET['customer_name']
        
        customers = customer_profile.objects.get(customer_name= name)
         
        context = {
                        
                        'my_customer': customers,
                    }
    return render(request, 'customer_profile.html', context)       

def create_supplier(request):
    
    if request.method == 'POST':
        form = SupplierForm(request.POST)
       
        if form.is_valid():
            form.save()
            return redirect('create_supplier')
    
    else:
        
        form = SupplierForm()
    return render(request, 'create_supplier.html', {'form': form })

def create_order(request):
    if request.method == 'POST':
        form = CosmicOrderForm(request.POST)
        print(form.data)
        if form.errors:
            print(form.errors) 

        if form.is_valid():
            print(form.data,"val")
            customers_name = request.POST.get('customer_name') 
            customer = customer_profile.objects.get(customer_name=customers_name)
            form.instance.customer_name = customer
            form.save()
            return redirect('create_order')  # Redirect to the list of purchases or any other desired view
        else:
            print(form.data,"nval")
            errors = dict(form.errors.items())
            return JsonResponse({'form_errors': errors}, status=400)
        
    form = CosmicOrderForm()
    formset = OrderItemForm()

    return render(request, 'create_order.html', {'form': form, 'formset': formset, 'customers': customers,'suppliers':suppliers})

def display_order(request):
    if request.method == 'GET':
        orders = cosmic_order.objects.all()
        orders = orders.order_by('order_no')

        orders_data = [orders]
        

    context = {
        'my_order': orders_data,
    }
    return render(request, 'display_order.html', context)

def create_order_items(request):
    
    if request.method == 'POST':
        formset = formset_factory(OrderItemForm, extra=1, min_num=1)
        
        formset = formset(request.POST or None,prefix="items")
        #print(formset.data,"r")
      
        if formset.errors:
            print(formset.errors)   
        
        # Check if 'PR_no' field is empty in each form within the formset
        for form in formset:
            print(form,"form")
        non_empty_forms = [form for form in formset if form.cleaned_data.get('item_name')]
       
        if non_empty_forms:
            print("yes")
            if formset.is_valid():
                final_quantity = 0.0
                pr_no = request.POST.get('order_no')
                print(pr_no,"pr")
                pr = cosmic_order.objects.get(order_no = pr_no)
                for form in non_empty_forms:
                    form.instance.remaining = form.cleaned_data['quantity']
                    form.instance.order_no = pr
                    final_quantity += form.cleaned_data['quantity']
                    
                    form.save()
                
                pr.total_quantity = final_quantity
                pr.remaining = final_quantity
                pr.save()
                #message.success("successful!")
            else:
                print(formset.data,"nval")
                errors = dict(formset.errors.items())
                return JsonResponse({'form_errors': errors}, status=400)
        
            pr_form = CosmicOrderForm(prefix="orders")
            formset = formset_factory(OrderItemForm, extra=1)
            formset = formset(prefix="items")

            context = {
                'pr_form': pr_form,
                'formset': formset,
                # 'message':success_message,
            }
            return render(request, 'create_order.html', context)
    else:
       
        formset = formset_factory(OrderItemForm, extra=1)
        formset = formset(prefix="items")

    context = {
        'formset': formset,
    }
    return render(request, 'create_order.html', context)

def display_single_order(request):
    if request.method == 'GET':
        pr_no = request.GET['order_no']
        orders = cosmic_order.objects.get(order_no=pr_no)
        pr_items = order_item.objects.all()
        pr_items = pr_items.filter(order_no=pr_no)
            
        
        if pr_items.exists():
            print(pr_items,"yes")
            context = {
                        'pr_items': pr_items,
                        'my_order': orders,
                    }
            return render(request, 'display_single_order.html', context)
        context = {
                        
                        'my_order': orders,
                    }
    return render(request, 'display_single_order.html', context)
