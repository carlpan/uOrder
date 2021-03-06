from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from .forms import UserForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            # Create user and save to database
            User.objects.create_user(username=username, password=password, email=email)
            # Authenticate the user
            user = authenticate(username=username, password=password)
            # Login the user
            login(request, user)
            # To be modified to redirect to home url
            return redirect(reverse('core:home'))
    else:
        form = UserForm()
    return render(request, 'authen/register.html', {'form': form})