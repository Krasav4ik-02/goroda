from django.urls import path
from .views import ProductImageView

urlpatterns = [
    path('api/products', ProductImageView.as_view() , name='product-image-view'),
]