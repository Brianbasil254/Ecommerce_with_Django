from itertools import product
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from . models import  Customer, Product

# Create your views here.
def product_list(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'Ecommerce/product_list.html', context)


def product_detail(request, pk):
    Product = get_object_or_404(Product, pk=pk)
    context = {
        'product': product
    }
    return render(request, 'Ecommerce/product_detail', context)

def customer_list(request):
    customers = Customer.objects.all()
    context = {
        'customers': customers
    }
    return render(request, 'Ecommerce/customer_list', context)

def customer_detail(request, pk):
    customer = get_object_or_404
    context ={
        'customers': customer
    }
    return render(request, 'Ecommerce/customer_detail', context )

