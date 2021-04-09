from django.shortcuts import render, get_object_or_404

from cart.forms import AddToCartForm
from shop.models import Product, Category


def home(request, slug=None):
    products = Product.available_products.all()
    categories = Category.objects.filter(is_sub=False)
    if slug:
        category = get_object_or_404(Category, slug=slug)
        products = Product.objects.filter(category=category)
    context = {
        'products': products,
        'categories': categories,
    }
    return render(request, 'shop/home.html', context)


def product_detail(request, product_id, slug):
    product = get_object_or_404(Product, id=product_id, slug=slug)
    form = AddToCartForm()
    context = {
        'product': product,
        'form': form,
    }
    return render(request, 'shop/product_detail.html', context)
