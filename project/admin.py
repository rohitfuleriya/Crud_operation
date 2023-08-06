from django.contrib import admin
from .models import Store, StoreProduct, StoreProductCategory
# Register your models here. 

@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ('store_id', 'store_name', 'store_tagline')



@admin.register(StoreProductCategory)
class StoreProductCategoryAdmin(admin.ModelAdmin):
    list_display = list_display = ('category_id', 'store', 'category_name', 'category_status')



@admin.register(StoreProduct)
class StoreProduct(admin.ModelAdmin):
    list_display = ('product_id', 'store', 'product_sku', 'product_name', 'product_stock', 'product_price')

