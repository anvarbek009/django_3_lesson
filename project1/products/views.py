from django.shortcuts import render
from .models import Products, Category
# Create your views here.

def home_page(request):
    categories = Category.objects.all()
    context={
        'categories': categories,
    }
    return render(request, 'index.html', context=context)

def get_products(request, pk):
    products = Products.objects.filter(category=pk)
    context={
        'products': products,
    }
    return render(request, 'products.html', context=context)