from django.urls import path, include

from shop import views, api_views

app_name = 'shop'

# api_urls = [
#         path('users', api_views.AllUsers.as_view()),
#         path('users/create', api_views.CreateUser.as_view()),
#         path('products', api_views.AllProduct.as_view()),
#         path('product/update/<int:pk>', api_views.UpdateProduct.as_view()),
#         path('product/delete/<int:pk>', api_views.DeleteProduct.as_view()),
# ]

urlpatterns = [
    path('', views.home, name='home'),
    path('<str:slug>', views.home, name='product_filter'),
    path('<int:product_id>/<str:slug>', views.product_detail, name='product_detail'),
    # path('api/', include(api_urls)),
]
