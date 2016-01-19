from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect
from django.http import HttpResponseBadRequest
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.forms import formset_factory
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.shortcuts import get_object_or_404
import json

from decorators import ajax_required
from custom import *
from .forms import UpdateItemQuantityForm
from merchants.models import Merchant

# Create your views here.

@login_required
def view_cart(request):
    cart = create_or_retrieve_cart(request)
    #cart = get_user_cart(request)

    cart_size = cart.size()
    #merchant = cart.merchant
    ItemQuantityFormSet = formset_factory(UpdateItemQuantityForm, extra=cart_size)

    if request.method == 'GET':
        return redirect(reverse('store:merchants'))


    return render(request, 'cart/newcart.html',
                  {'cart': cart, 'ItemQuantityFormSet': ItemQuantityFormSet})


@login_required
def add_to_cart(request):
    if request.method == 'POST':
        menuitem_id = request.POST.get('item_id')
        quantity = request.POST.get('item_quantity')
        merchant_id = request.POST.get('merchant_id')
        merchant = get_object_or_404(Merchant, pk=merchant_id)

        # retrieve cart first
        '''
        cart = get_user_cart(request)
        if cart:
            # check associated merchant
            if cart.merchant != merchant:
                messages.warning(request, 'You current cart will be discarded.')
                cart.delete()
                cart = create_user_cart(request, merchant)
        else:
            cart = create_user_cart(request, merchant)
        '''
        cart = create_or_retrieve_cart(request)
        cart.create_or_update_cart_item(menuitem_id, quantity)
        cart.save()

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

        response_data = {}
        response_data['size'] = cart.size()
        return HttpResponse(json.dumps(response_data), content_type="application/json")
    except Exception, e:
        return HttpResponseBadRequest()


@login_required
def update_cart(request):
    cart = create_or_retrieve_cart(request)
    cart_size = cart.size()
    ItemQuantityFormSet = formset_factory(UpdateItemQuantityForm, extra=cart_size)

    if request.method == 'POST' and request.is_ajax():
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

            response_data = {}
            response_data['success'] = 'Get back successfully'
            return HttpResponse(json.dumps(response_data), content_type="application/json")
    else:
        return HttpResponse("")
    #return redirect(reverse('cart:view_cart'))





