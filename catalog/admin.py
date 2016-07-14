from django.contrib import admin
from catalog.models import Category, Product, Brand, Banner

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','sort_order','status','created_at','updated_at')
    # list_filter = ('owner','active')
    # list_search = ('name',)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name','created_at','updated_at')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','sku','price','brand','category','status','created_at','updated_at')    

class BannerAdmin(admin.ModelAdmin):
    list_display = ('name','status','sort_order','created_at','updated_at')

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Banner, BannerAdmin)
