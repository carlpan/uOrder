from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from .forms import LoginForm, ProfileForm, ChangeAccountForm

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

@login_required
def profile_settings(request):
    user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.userprofile.location = form.cleaned_data['location']
            user.save()
            messages.add_message(request, messages.SUCCESS, 'Your profile were successfully edited.')
    else:
        form = ProfileForm(instance=user)
    return render(request, 'core/profile.html', {'form': form})

@login_required
def account_settings(request):
    user = request.user
    if request.method == 'POST':
        form = ChangeAccountForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['new_username']:
                user.username = form.cleaned_data['new_username']
            if form.cleaned_data['new_email']:
                user.email = form.cleaned_data['new_email']
            new_password = form.cleaned_data['new_password']
            user.set_password(new_password)
            user.save()
            messages.add_message(request, messages.SUCCESS, 'Your account were successfully changed.')
    else:
        form = ChangeAccountForm(instance=user, initial={
            'new_username': user.username,
            'new_email': user.email
        })
    return render(request, 'core/account.html', {'form': form})