from django.shortcuts import render, HttpResponse
from . models import Product, Category, Customer, Order

# Create your views here.
def index(request) -> HttpResponse:
    products = Product.objects.all()
    categories = Category.objects.all()
    customers = Customer.objects.all()
    orders = Order.objects.all()

    return render(request, 'eshop/index.html', {
        'products' : products,
        'categories' : categories,
        'customers' : customers,
        'orders' : orders,
    })



def vypis_products(request) -> HttpResponse:
    products = Product.objects.all()
    return render(request, 'eshop/index.html', {
        'products' : products,
    })

def vypis_categories(request) -> HttpResponse:
    categories = Category.objects.all()
    return render(request, 'eshop/index.html', {
        'categories' : categories,
    })

def vypis_customers(request) -> HttpResponse:
    customers = Customer.objects.all()
    return render(request, 'eshop/index.html', {
        'customers' : customers,
    })  

def category(request, category):
    categories = Category.objects.all()
    category_obj = Category.objects.get(name=category)
    products = Product.objects.filter(category_id=category_obj.pk).order_by("name")
    return render(request, "eshop/index.html", {"categories" : categories, "products" : products, "special_message" : f"Výsledky pre kategóriu {category_obj.name}"})

def product(request, product):
    product_obj = Product.objects.get(name=product)
    return render(request, "eshop/product.html", {"product" : product_obj})
