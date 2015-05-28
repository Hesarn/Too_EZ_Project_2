from django.shortcuts import render, get_object_or_404
from users.forms import loginForm, signupForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from users.models import Film
from django import forms
from users.models import MyUser
from django.contrib.auth.decorators import login_required
# Create your views here.

# YEARS = ['Year'] + list(range(2015, 1940, -1))
# MONTHS = ('Month', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')
# DAYS = ['Day'] + list(range(1, 32))

def login_user(request):
    if request.method == "POST":
        form = loginForm(request.POST)

        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])

            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('timeLine'))

            else:
                form.add_error(None, 'Entered username or password is wrong')
                return render(request, 'signin.html', {'form': form})

        else:
            return render(request, 'signin.html', {'form': form})

    else:
        form = loginForm()
        return render(request, 'signin.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = signupForm(request.POST)
        if form.is_valid():
            newUser = MyUser()

            try:
                _newUser = User.objects.create_user(username=request.POST['username'], password=request.POST['password']
                                                    , first_name=request.POST['name'], email=request.POST['email'])
                newUser.user = _newUser
                newUser.birthday = request.POST['birthday_day'] + '/' + request.POST['birthday_month'] + '/' + \
                                   request.POST['birthday_year']
                newUser.save()

            except:
                form.add_error(None, 'username "' + request.POST['username'] + '" already existed')
                return render(request, 'signup.html', {'signupForm': form})

            return HttpResponseRedirect(reverse('login'))

        else:
            return render(request, 'signup.html', {'signupForm': form})

    else:
        form = signupForm()
        return render(request, 'signup.html', {'signupForm': form})


def forget(request):
    return render(request, 'forget.html', {})


@login_required()
def timeLine(request):
    return render(request, 'timeline.html', {'user': MyUser.objects.get(user=request.user)})


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))

@login_required()
def movie_profile(request, filmName):
    return render(request, 'movieProfile.html', {'film': get_object_or_404(Film, name=filmName),
                                                 'user': get_object_or_404(MyUser, user=request.user)})