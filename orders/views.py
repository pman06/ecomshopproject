from django.shortcuts import render
from django.contrib import messages
from .models import Order, OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
# Create your views here.

def order_create(request):
    cart= Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            print(cart)
            if cart:
                order = form.save()
                for item in cart:
                    OrderItem.objects.create(order=order, product=item['product'], price=item['price'], quantity=item['quantity'])
                    #clear the cart
                    cart.clear()
                    return render(request, 'orders/order/created.html', {'order':order})
            else:
                #if no product is added to cart, return an error message to the user.
                message ='Your cart is empty. Please <a href="/">add products to cart.</a>'
                messages.error(request, message)
    else:
        form = OrderCreateForm()
    return render(request, 'orders/order/create.html', {'cart':cart,'form':form})
