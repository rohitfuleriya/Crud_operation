from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StoreListCreateView, StoreProductCategoryView, StoreProductView
from .import views
router = DefaultRouter()
router.register('stores', StoreListCreateView)
router.register('category', StoreProductCategoryView)
router.register('product', StoreProductView)


urlpatterns = [
    path('', include(router.urls)),
    path('stores/<str:store_id>/category/', views.store_categories, name='store-categories'),
    path('stores/<str:store_id>/product/', views.store_products, name='store-products'),

    
]