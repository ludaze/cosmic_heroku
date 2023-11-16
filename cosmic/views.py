from django.shortcuts import render

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
        form = OrderItemForm(request.POST)
        print(form.data)
        if form.errors:
            print(form.errors) 

        if form.is_valid():
            print(form.data,"val")
            order_no = request.POST.get('order_no') 
            order_no= = cosmic_cosmic_order.objects.get(order_no=order_no)
            form.instance.order_no = order_no
            form.save()
            return redirect('create_order')  # Redirect to the list of purchases or any other desired view
        else:
            print(form.data,"nval")
            errors = dict(form.errors.items())
            return JsonResponse({'form_errors': errors}, status=400)

            context = {
                'pr_form': pr_form,
                'formset': formset,
                # 'message':success_message,
            }
            return render(request, 'create_order.html', context)
    else:
       
        form = OrderItemForm()

    context = {
        'formset': formset,
    }
    return render(request, 'create_order.html', context)
