from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib import messages
# from django.contrib.auth.models import login_required
from .models import Order, OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from .tasks import order_created
# Create your views here.

def order_create(request):
    cart= Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            if cart:
                order = form.save()
                for item in cart:
                    OrderItem.objects.create(order=order, product=item['product'], price=item['price'], quantity=item['quantity'])
                    #clear the cart
                    cart.clear()

                    #launch asynchronous task
                    order_created.delay(order.order_id)
                    #set the order in the session
                    request.session['order_id'] = order.id
                    #redirect for payment
                    return redirect(reverse('payment:process'))
            else:
                #if no product is added to cart, return an error message to the user.
                message ='Your cart is empty. Please <a href="/">add products to cart.</a>'
                messages.error(request, message)
    else:
        form = OrderCreateForm()
    return render(request, 'orders/order/create.html', {'cart':cart,'form':form})
