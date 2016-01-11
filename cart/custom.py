import datetime

from .models import Cart, CartItem

CART_ID = 'CART_ID'

def create_or_retrieve_cart(request):
    cart_id = request.session.get(CART_ID)
    if cart_id:
        try:
            cart = Cart.objects.get(id=cart_id, checked_out=False)
        except Cart.DoesNotExist:
            cart = create_new_cart(request)
    else:
        cart = create_new_cart(request)
    return cart

def create_new_cart(request):
    cart = Cart(creation_date=datetime.datetime.now())
    cart.save()
    request.session[CART_ID] = cart.id
    return cart