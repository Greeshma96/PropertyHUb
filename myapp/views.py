# myapp/views.py
from django.shortcuts import render,redirect
from .models import Property, Tenant,Unit
from .forms import PropertyForm,UnitForm,TenantForm

def listing(request):
    properties = Property.objects.all()
    return render(request, 'listing.html', {'properties': properties})

def property_detail(request, property_id):
    property_obj = Property.objects.get(pk=property_id)
    return render(request, 'property_detail.html', {'property': property_obj})

def tenant_management(request):
    tenants = Tenant.objects.all()
    return render(request, 'tenant.html', {'tenants': tenants})

def add_property(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('property_listing')
    else:
        form = PropertyForm()

    return render(request, 'add.html', {'form': form})


def add_unit(request, property_id):
    property_obj = Property.objects.get(pk=property_id)

    if request.method == 'POST':
        form = UnitForm(request.POST)
        if form.is_valid():
            unit = form.save(commit=False)
            unit.property = property_obj
            unit.save()
            return redirect('property_detail', property_id=property_id)
    else:
        form = UnitForm()

    return render(request, 'unit.html', {'form': form, 'property': property_obj})

def add_tenant(request, unit_id):
    unit_obj = Unit.objects.get(pk=unit_id)

    if request.method == 'POST':
        form = TenantForm(request.POST)
        if form.is_valid():
            tenant = form.save(commit=False)
            tenant.unit = unit_obj
            tenant.save()
            return redirect('property_detail', property_id=unit_obj.property.id)
    else:
        form = TenantForm()
    return render(request, 'addtenant.html', {'form': form, 'unit': unit_obj})


