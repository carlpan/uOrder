from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
import datetime

from .models import *

# Create your views here.

@login_required
def merchants(request):
    all_merchants = Merchant.objects.all()
    return render(request, 'merchants/merchants.html', {'merchants': all_merchants})

def merchant(request, merchant_name, pk):
    merchant = get_object_or_404(Merchant, pk=pk)

    '''
    Dealing with merchant hour info.
    '''
    now = datetime.datetime.now()
    open_status = is_open(pk, now)
    business_hours = get_business_hour(pk, now.isoweekday())
    from_hour = business_hours['from_hour']
    to_hour = business_hours['to_hour']

    '''
    Dealing with menu items
    '''
    categories = merchant.menucategory_set.all()

    return render(request, 'merchants/merchant.html',
                  {'merchant': merchant, 'status': open_status,
                   'from_hour': from_hour, 'to_hour': to_hour,
                   'categories': categories})

