from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
import datetime
import json

from .models import Cart, CartItem
from custom import *

# Create your views here.

@login_required
def view_cart(reqest):
    pass

@login_required
def add_to_cart(request):
    if request.method == 'POST':
        menuitem_id = request.POST.get('item_id')
        quantity = request.POST.get('item_quantity')

        # create or retrieve cart
        cart = create_or_retrieve_cart(request)
        cart.create_or_update_cart_item(menuitem_id, quantity)

        # prepare json for return
        response_data = {}
        response_data['count'] = cart.size()

        return HttpResponse(json.dumps(response_data), content_type="application/json")
    else:
        return HttpResponse("")