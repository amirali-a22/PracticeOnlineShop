from django.urls import path

from orders import views

app_name = 'orders'

urlpatterns = [
    path('order-detail/<int:order_id>', views.order_detail, name='order_detail'),
    path('orer-create', views.order_create, name='order_create'),
]
