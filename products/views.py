from django.shortcuts import render,get_object_or_404
from .models import Product,Category


def home(request):

    products = Product.objects.all()

    categories = Category.objects.all()

    return render(request,"home.html",{
        "products":products,
        "categories":categories
    })


def category_products(request,id):

    category = Category.objects.get(id=id)

    products = Product.objects.filter(category=category)

    categories = Category.objects.all()

    return render(request,"home.html",{
        "products":products,
        "categories":categories
    })


def product_detail(request,id):

    product = get_object_or_404(Product,id=id)

    categories = Category.objects.all()

    return render(request,"products/product_detail.html",{
        "product":product,
        "categories":categories
    })