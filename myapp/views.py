from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import *
from .forms import *
from django.shortcuts import render, redirect, get_object_or_404
def home(request):
    return render(request, 'myapp/home.html')

def product_list(request):
    q = request.GET.get('q', '')
    if q:
        products = product.objects.filter(product_name__icontains=q)
    else:
        products = product.objects.all()
    context = {
        'products': products
    }
    return render(request, template_name='myapp/all_product.html', context=context)

def product_details(request, id):
    product_obj = get_object_or_404(product, pk=id)
    context = {
        'product': product_obj,
    }
    return render(request, template_name='myapp/details_product.html', context=context)

def upload_product(request):
    form = productForm()
    if request.method == 'POST':
        form = productForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    context = {'form': form}
    return render(request, template_name='myapp/product_form.html', context=context)

def update_product(request, id):
    product_instance = get_object_or_404(product, pk=id)
    form = productForm(instance=product_instance)
    if request.method == 'POST':
        form = productForm(request.POST, request.FILES, instance=product_instance)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    context = {'form': form}
    return render(request, template_name='myapp/product_form.html', context=context)

def delete_product(request, id):
    product_instance = get_object_or_404(product, pk=id)
    if request.method == 'POST':
        product_instance.delete()
        return redirect('product_list')
    context = {'product': product_instance}
    return render(request, 'myapp/delete_product.html', context)


def booknow(request):
    return render(request, 'myapp/booknow.html')

def loyality(request):
    return render(request, 'loyality.html')

def membership(request):
    return render(request, 'membership.html')

def detailing(request):
    return render(request, 'detailing.html')

@login_required
def become_member(request):
    if request.method == "POST":
        membership_type = request.POST.get("membership_type")
        user = request.user
        user.membership_type = membership_type
        user.save()
        # Optionally, add a success message
    return redirect('profile')



@login_required
def rent_product(request, product_id):
    product_obj = get_object_or_404(product, pk=product_id)
    if request.method == "POST":
        # You can expand this logic to actually create a CarRental object if needed
        # For now, just redirect to profile or show a success message
        return redirect('profile')
    context = {
        'product': product_obj,
    }
    return render(request, 'myapp/booknow.html', context)

def autowash(request):
    return render(request, 'autowash.html')

def garage(request):
    return render(request, 'garage.html')