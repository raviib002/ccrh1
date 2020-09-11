from django.contrib.auth import authenticate
from django.contrib.auth.forms import (AuthenticationForm, PasswordResetForm)

from django.contrib.auth.forms import (AuthenticationForm, UserCreationForm, 
                                       UserChangeForm, PasswordResetForm, 
                                       SetPasswordForm, PasswordChangeForm)
from django import forms
from django.contrib.auth.models import User, Group
from django.utils.translation import ugettext_lazy as _


class LoginForm(AuthenticationForm):
    username = forms.CharField(required=True, label=_("Email"), max_length=254, widget=forms.TextInput(attrs={'class':'form-control lowercase','placeholder': 'Email'}))
    password = forms.CharField(required=True, label=_("Password"), widget=forms.PasswordInput(attrs={'class':'form-control','id':'password','placeholder': 'Password'}))
   
    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        
        if username and password:
            self.user_cache = authenticate(username=username, password=password)
        return self.cleaned_data
    
"""For password reset form having email field"""
class PasswordResetFormUnique(PasswordResetForm):
    email = forms.EmailField(label=_("Email"), max_length=254, widget=forms.TextInput(attrs={'class':'email form-control', 'placeholder':'Email', 'style':'text-transform:none;'}))

"""For password reset form having passwords field"""    
class CustomPasswordChangeForm(PasswordChangeForm):
    new_password1 = forms.CharField(
        label=_("New Password"),
        widget=forms.PasswordInput(attrs={'class':'form-control ', 'id':'newpassword1', 'placeholder': 'New Password'})
    )
    new_password2 = forms.CharField(
        label=_("Confirm New Password"),
        widget=forms.PasswordInput(attrs={'class':'form-control', 'id':'newpassword2', 'placeholder': 'Confirm New Password'})
    )
    old_password = forms.CharField(
        label=_("Current Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'class':'form-control', 'id':'oldpassword', 'placeholder': 'Current Password'}),
    )

    field_order = ['old_password', 'new_password1', 'new_password2']
    
    
class CustomSetPasswordForm(forms.Form):
    new_password1 = forms.CharField(
        label=_("New password"),
        widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'New Password', 'id':'newpassword1'})
    )
    new_password2 = forms.CharField(
        label=_("New password confirmation"),
        widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Confirm New Password', 'id':'newpassword2'})
    )
        