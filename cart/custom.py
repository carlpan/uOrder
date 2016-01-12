import datetime

from .models import Cart

#CART_ID = 'CART_ID'

def get_user_cart(request):
    user = request.user
    cart = Cart.objects.get(user=user, checked_out=False)
    return cart

def create_user_cart(request):
    cart = Cart(creation_date=datetime.datetime.now())
    cart.user = request.user
    cart.save()
    return cart

def create_or_retrieve_cart(request):
    if request.user.is_authenticated():
        try:
            cart = get_user_cart(request)
        except Cart.DoesNotExist:
            cart = create_user_cart(request)
    else:
        cart = create_user_cart(request)
    return cart


'''
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
'''