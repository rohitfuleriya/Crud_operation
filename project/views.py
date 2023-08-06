from rest_framework import viewsets
from rest_framework.response import Response
from .models import Store, StoreProductCategory, StoreProduct
from .serializers import StoreSerializer, StoreProductCategorySerializer, StoreProductSerializer
from rest_framework.decorators import api_view
# Create your views here.



class StoreListCreateView(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    lookup_field = 'store_id'



class StoreProductCategoryView(viewsets.ModelViewSet):
    queryset = StoreProductCategory.objects.all()
    serializer_class = StoreProductCategorySerializer


@api_view(['GET'])
def store_categories(request, store_id):
    categories = StoreProductCategory.objects.filter(store__store_id=store_id)
    serializer = StoreProductCategorySerializer(categories, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def store_products(request, store_id):
    products = StoreProduct.objects.filter(store__store_id=store_id)
    serializer = StoreProductSerializer(products, many=True)
    return Response(serializer.data)


class StoreProductView(viewsets.ModelViewSet):
    queryset  = StoreProduct.objects.all()
    serializer_class = StoreProductSerializer
    
    




    