from django.shortcuts import render
from catalog.models import Category, Product, Brand, Banner

def index(request):
    return render(request, 'index.html', {'categorys':getcategorys, 'banners':getbanner, 'products':allproducts})

def category(request,category_id):
    return render(request, 'category.html', {'category':getcategory(category_id),'products':getproducts(category_id), 'categorys':getcategorys, 'brands':getbrands(getproducts(category_id))})
def catmain(request):
    return render(request, 'category.html', {'categorys':getcategorys})

def getcategory(category_id):
    category = Category.objects.get(pk=category_id)
    return category
def allproducts():
    products = Product.objects.all()
    return products
def getproducts(category_id):
    products = Product.objects.filter(category__id=category_id)
    return products
def getcategorys():
    categorys = Category.objects.filter(status=1).order_by('sort_order')
    return categorys
def getbanner():
    banners = Banner.objects.all()
    return banners
def getbrands(products):
    brands = list();
    brandes = Brand.objects.all()
    for product in products:
        for brand in brandes:
            if (brand.name == product.brand.name):
                brands.append(brand) 
    return brands
