from django import forms
from django.forms import PasswordInput
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.forms.extras.widgets import SelectDateWidget
from captcha.fields import CaptchaField


class loginForm(forms.Form):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'name': "user",
                                            'placeholder': 'Username or Email', 'class': 'input'}))

    password = forms.CharField(label='', widget=PasswordInput(attrs={'name': "login",
                                            'placeholder': 'Password', 'class': 'input'}))


class signupForm(forms.Form):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'input'}))
    name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Name', 'class': 'input'}))
    email = forms.EmailField(label='', widget=forms.TextInput(attrs={'placeholder': 'Email', 'class': 'input'}))
    password = forms.CharField(label='', widget=PasswordInput(attrs={'placeholder': 'Password', 'class': 'input'}))
    confirmPassword = forms.CharField(label='', widget=PasswordInput(attrs={'placeholder': 'Confirm Password',
                                                                             'class': 'input'}))

    birthday = forms.DateField(widget=SelectDateWidget(years=list(range(2015, 1930, -1))))
    captcha = CaptchaField()


    def clean(self):
        password = self.data['password']
        cpassword = self.data['confirmPassword']

        if password!='' and cpassword!='' and password != cpassword:
            raise forms.ValidationError("Entered passwords do not match.")




