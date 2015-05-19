from django.shortcuts import render
from user.forms import LoginForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate
from django import forms

# Create your views here.

def login(request):
    if(request.method=="POST"):
        form = LoginForm(request.POST)

        if form.is_valid():
            user = authenticate(username=form.data['username'], password=form.data['password'])

            return render(request, 'timeline.html', {'user': user})

        else:
            return render(request, 'signin.html', {'form': form})

    else:
        form = LoginForm()
        return render(request, 'signin.html', {'form': form})

def signup(request):
    return render(request, 'signup.html', {})

def forget(request):
    return render(request, 'forget.html', {})




