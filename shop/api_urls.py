from django.urls import path
from rest_framework import routers

from shop.api_views import UserViewSet, ProductViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet, basename='users')
router.register('products', ProductViewSet)
