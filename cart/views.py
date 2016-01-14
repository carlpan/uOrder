from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect
from django.http import HttpResponseBadRequest
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.forms import formset_factory
from django.core.urlresolvers import reverse
import json

from decorators import ajax_required
from custom import *
from .forms import UpdateItemQuantityForm

# Create your views here.

@login_required
def view_cart(request):
    cart = create_or_retrieve_cart(request)
    cart_size = cart.size()
    ItemQuantityFormSet = formset_factory(UpdateItemQuantityForm, extra=cart_size)

    return render(request, 'cart/cart.html',
                  {'cart': cart, 'ItemQuantityFormSet': ItemQuantityFormSet})


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
        response_data['count'] = cart.aggregate_cart_size()

        return HttpResponse(json.dumps(response_data), content_type="application/json")
    else:
        return HttpResponse("")


@login_required
@csrf_exempt
def remove_item(request):
    cart = create_or_retrieve_cart(request)
    try:
        cartitem_id = request.POST.get('cartitem')
        cartitem = cart.retrieve_cart_item(cartitem_id)
        cartitem.delete()
        cart.save()
        return HttpResponse()
    except Exception, e:
        return HttpResponseBadRequest()


@login_required
def update_cart(request):
    cart = create_or_retrieve_cart(request)
    cart_size = cart.size()
    ItemQuantityFormSet = formset_factory(UpdateItemQuantityForm, extra=cart_size)

    if request.method == 'POST':
        formset = ItemQuantityFormSet(request.POST)
        if formset.is_valid():
            # loop each form in formset
            for form in formset:
                quantity = form.cleaned_data.get('quantity')
                cartitem_id = form.cleaned_data.get('cartitem')
                cartitem = cart.retrieve_cart_item(cartitem_id=cartitem_id)
                if cartitem.quantity != quantity:
                    cartitem.update_quantity(quantity)
            # save the cart update
            cart.save()

    return redirect(reverse('cart:view_cart'))





