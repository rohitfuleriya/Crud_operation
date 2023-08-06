from django.db import models
import uuid 
# Create your models here.

class Store(models.Model):
    store_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    store_owner_id = models.UUIDField(default=uuid.uuid4, editable=False)
    store_name = models.CharField(max_length=255)
    store_logo = models.ImageField(upload_to='store_logo/')
    store_tagline = models.CharField(max_length=255)
    store_about_us = models.TextField()

    def __str__(self):
        return self.store_name


class StoreProductCategory(models.Model):
    category_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    category_name = models.CharField(max_length=255)
    category_image = models.ImageField(upload_to='category_store/')
    category_description = models.TextField()
    category_name_of_products = models.IntegerField(default=0)
    category_status = models.BooleanField()


    def __str__(self):
        return self.category_name
    


class StoreProduct(models.Model):
    product_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    product_sku = models.CharField(max_length=50)
    product_name = models.CharField(max_length=255)
    product_primary_image = models.ImageField(upload_to='product_imgages/')
    product_images = models.ImageField(upload_to='product_images/', blank=True, null=True)
    product_description = models.TextField()
    product_stock = models.BooleanField()
    product_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.product_name



    