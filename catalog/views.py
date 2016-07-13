from django.shortcuts import render
from catalog.models import Category, Product, Brand, Banner

def index(request):
    return render(request, 'index.html', {'categorys':getcategorys})

def category(request,category_id):
    return render(request, 'category.html', {'category':getcategory(category_id),'products':getproducts(category_id), 'categorys':getcategorys()})

def getcategory(category_id):
    category = Category.objects.get(pk=category_id)
    return category
def getproducts(category_id):
    products = Product.objects.filter(category__id=category_id)
    return products
def getcategorys():
    categorys = Category.objects.all().order_by('sort_order')
    return categorys