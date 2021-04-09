from django.urls import path

from cart import views

app_name = 'cart'

urlpatterns = [
    path('cart-detail', views.cart_detail, name='cart_detail'),
    path('cart-add/<int:product_id>', views.cart_add, name='cart_add'),
    path('remove/<int:product_id>', views.remove_product, name='remove_product'),
]
