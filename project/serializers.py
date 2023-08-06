from rest_framework import serializers
from .models import Store, StoreProductCategory, StoreProduct


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = '__all__'



class StoreProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreProductCategory
        fields = '__all__'


class StoreProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreProduct
        fields = '__all__'