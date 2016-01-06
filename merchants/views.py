from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Merchant

# Create your views here.

def merchants(request):
    all_merchants = Merchant.objects.all()
    return render(request, 'merchants/merchants.html', {'merchants': all_merchants})

def merchant(request, pk):
    merchant = get_object_or_404(Merchant, pk=pk)
    return render(request, 'merchants/merchant.html', {'merchant': merchant})