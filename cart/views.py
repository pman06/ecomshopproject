from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.decorators.http import require_POST
from django.contrib import messages
from shop.models import Product
from .cart import Cart
from coupons.forms import CouponApplyForm
from .forms import CartAddProductForm
from django.utils.safestring import mark_safe
# Create your views here.

@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'], override_quantity=cd['override'])
        url = reverse("shop:product_list")
        message = mark_safe(f'Product added to cart successfully. <a href="{url}">Continue Shopping</a>')
        messages.success(request, message)
    return redirect('cart:cart_detail')

@require_POST
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id =product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail_view(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={
            'quantity':item['quantity'],
            'override':True})
    coupon_apply_form = CouponApplyForm()
    return render(request,'cart/detail.html', {'cart':cart, 'coupon_apply_form':coupon_apply_form})
