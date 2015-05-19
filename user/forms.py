from django import forms
from django.forms import PasswordInput
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class LoginForm(forms.Form):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'name': "user",
                                'placeholder': 'Username or Email', 'class': 'input'}), required=False)

    password = forms.CharField(label='', widget=PasswordInput(attrs={'name': "login",
                                'placeholder': 'Password', 'class': 'input'}), required=False)

    def clean_username(self):
        if len(self.data['username'])==0:
            self.add_error('username', 'This field is empty')

    def clean_password(self):
        if len(self.data['password'])==0:
            self.add_error('password', 'This field is empty')

    def clean(self):
        if self.data['username']!='' and self.data['password']!='':
            user = authenticate(username=self.data['username'], password=self.data['password'])

            if user is None:
                raise forms.ValidationError('Entered username or password is wrong')



