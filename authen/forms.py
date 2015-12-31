from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# Validators
def InvalidUsernameValidator(value):
    if '@' in value or '+' in value or '-' in value:
        raise ValidationError("Please enter a valid username.")

def UniqueUsernameValidator(value):
    if User.objects.filter(username__iexact=value).exists():
        raise ValidationError("User already exists.")

def UniqueEmailValidator(value):
    if User.objects.filter(email__iexact=value).exists():
        raise ValidationError("User with this email already exists.")


# User registration
class UserForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
                               max_length=30, required=True)
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
                            max_length=75, required=True)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
                               required=True)
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                         'placeholder': 'Confirm Password'}),
                                       required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirm_password']

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['username'].validators.append(InvalidUsernameValidator)
        self.fields['username'].validators.append(UniqueUsernameValidator)
        self.fields['email'].validators.append(UniqueEmailValidator)

    def clean(self):
        super(UserForm, self).clean()
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password and password != confirm_password:
            self._errors['password'] = self.error_class(['Password don\'t match.'])
        return self.cleaned_data
