from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.urlresolvers import reverse

from .forms import LoginForm

# Create your views here.

# Index page with login form displayed.
def index(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.login(request)

            if user:
                login(request, user)
                return redirect(reverse('core:home'))
    else:
        form = LoginForm()
    return render(request, 'core/index.html', {'form': form})

# Save login logic but with designated login url
def user_login(request):
    form = LoginForm(request.POST or None)
    if request.POST and form.is_valid():
        user = form.login(request)
        if user:
            login(request, user)
            return redirect(reverse('core:home'))
    return render(request, 'core/index.html', {'form': form})

# Logout logic
def user_logout(request):
    logout(request)
    return redirect(reverse('core:index'))

# Home page upon successful login
def home(request):
    if request.user.is_authenticated():
        return render(request, 'core/home.html', {})
    else:
        return render(request, 'core/index.html')