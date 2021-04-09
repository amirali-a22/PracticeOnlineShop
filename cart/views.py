from django.shortcuts import render, get_object_or_404, redirect

from cart.cart import Cart
from cart.forms import AddToCartForm
from shop.models import Product

from django.views.decorators.http import require_POST


def cart_detail(request):
    cart = Cart(request)
    context = {
        'cart': cart
    }
    return render(request, 'cart/cart_detail.html', context)


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = AddToCartForm(request.POST)
    if form.is_valid():
        cart.add(product, form.cleaned_data['quantity'])
    return redirect('cart:cart_detail')


def remove_product(request, product_id):
    cart = Cart(request)
    cart.remove(product_id)
    return redirect('cart:cart_detail')
