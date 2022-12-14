from django import forms
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.Form):
      username = forms.CharField(
        label='Username',
        widget=forms.TextInput(
            attrs={
                'autocomplete': 'username',
            }
        )
    )
      email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(
              attrs={
                'autocomplete': 'email',
            }
            
        )
    )     
    
      password = forms.CharField(
            label='Password',
            max_length=50,
            widget=forms.PasswordInput(attrs={'autocomplete': 'password'})
      )
      password_confirm = forms.CharField(
        label='Confirm Password',
        max_length=50,
        widget=forms.PasswordInput,
    )

class LoginForm(forms.Form):
    '''Form for user login'''

    username = forms.CharField(
        label='Username',
        max_length=50,
        widget=forms.TextInput(attrs={'autocomplete': 'username'})
    )
    password = forms.CharField(
        label='Password',
        max_length=50,
        widget=forms.PasswordInput(attrs={'autocomplete': 'password'})
    )

    
    