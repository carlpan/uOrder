from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from cart.custom import get_user_cart
from .models import OrderItem
from .forms import CreateOrderForm

# Create your views here.
@login_required
def create_order(request):
    # get cart
    cart = get_user_cart(request)
    if request.method == 'POST':
        form = CreateOrderForm(request.POST)
        if form.is_valid():
            # saves order object from form data
            order = form.save()
            for item in cart.cartitem_set.all():
                OrderItem.objects.create(order=order,
                                         menu_item=item.menu_item,
                                         price=item.menu_item.entry_price,
                                         quantity=item.quantity)

            # clear the cart after saving order items
            cart.empty_cart()
            return render(request, 'orders/checkout.html', {'order': order})
    else:
        merchant = cart.merchant
        form = CreateOrderForm()
    return render(request, 'orders/checkout.html', {'form': form, 'merchant': merchant})



