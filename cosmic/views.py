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

def create_supplier(request):
    
    if request.method == 'POST':
        form = SupplierForm(request.POST)
       
        if form.is_valid():
            form.save()
            return redirect('create_supplier')
    
    else:
        
        form = SupplierForm()
    return render(request, 'create_supplier.html', {'form': form })
