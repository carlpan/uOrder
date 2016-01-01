from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from authen.forms import InvalidUsernameValidator, UniqueUsernameValidator, UniqueEmailValidator


# User Login
class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
                               max_length=30, required=True)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
                               required=True)

    #class Meta:
    #    model = User
    #    fields = ['username', 'password']

    def clean(self):
        super(LoginForm, self).clean()
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user or not user.is_active:
            raise forms.ValidationError("Login was invalid. Please try again.")
        return self.cleaned_data

    def login(self, request):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        return user

# Profile form
class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),
                                 max_length=30, required=False)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),
                                max_length=30, required=False)
    location = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),
                               max_length=50, required=False)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'location']

# Change user account
class ChangeAccountForm(forms.ModelForm):
    id = forms.CharField(widget=forms.HiddenInput())
    new_username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),
                                   max_length=30, label="Username", required=False)
    new_email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control'}),
                                max_length=50, label="Email", required=False)
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                     'placeholder': 'Current password'}),
                                   label="Password", required=True)
    new_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                     'placeholder': 'New password'}),
                                   required=True)
    confirm_new_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                             'placeholder': 'Confirm new password'}),
                                           required=True)

    class Meta:
        model = User
        fields = ['id', 'new_username', 'new_email', 'old_password', 'new_password', 'confirm_new_password']

    # Append validators on single form field
    def __init__(self, *args, **kwargs):
        super(ChangeAccountForm, self).__init__(*args, **kwargs)
        self.fields['new_username'].validators.append(InvalidUsernameValidator)

    # Adding validation logic on depending fields
    def clean(self):
        super(ChangeAccountForm, self).clean()
        old_password = self.cleaned_data.get('old_password')
        new_password = self.cleaned_data.get('new_password')
        confirm_new_password = self.cleaned_data.get('confirm_new_password')
        id = self.cleaned_data.get('id')
        user = User.objects.get(pk=id)

        # Perform validation
        if not user.check_password(old_password):
            msg = "Old password don't match"
            self.add_error('old_password', msg)
        if new_password and new_password != confirm_new_password:
            msg = "Passwords don't match"
            self.add_error('new_password', msg)
            self.add_error('confirm_new_password', msg)
        return self.cleaned_data
