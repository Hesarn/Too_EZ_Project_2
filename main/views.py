from django.shortcuts import render, get_object_or_404
from users.forms import loginForm, signupForm
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from users.models import Film
from django import forms
from users.models import MyUser, Post, Comment
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import json
from django.template import Context, Template

from django.core.serializers.json import DjangoJSONEncoder

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


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))


@login_required()
def timeLine(request):
    followingUsers = MyUser.objects.get(user=request.user).followingUsers.all()
    posts = Post.objects.filter(user=followingUsers).order_by('-pubDate')[:1]

    return render(request, 'timeline.html', {'currUser': MyUser.objects.get(user=request.user), 'posts': posts})


@login_required()
def movie_profile(request, filmName):
    return render(request, 'movieProfile.html', {'film': get_object_or_404(Film, name=filmName),
                                                 'currUser': get_object_or_404(MyUser, user=request.user)})


@login_required()
def show_post(request, userID, postID):
    return render(request, 'post.html', {'user': get_object_or_404(MyUser, id=userID),
                                         'currUser': get_object_or_404(MyUser, user=request.user),
                                         'post': get_object_or_404(Post, id=postID)})


@login_required()
def show_user_profile(request):
    return render(request, 'userProfile.html', {'user': get_object_or_404(MyUser, user=request.user),
                                                'currUser': get_object_or_404(MyUser, user=request.user),
                                                'isThisUser': True})

@login_required()
def show_other_profiles(request, userID):
    if get_object_or_404(MyUser, user=request.user) == get_object_or_404(MyUser, id=userID):
        return show_user_profile(request)

    else:
        return render(request, 'userProfile.html', {'user': get_object_or_404(MyUser, id=userID),
                                                'currUser': get_object_or_404(MyUser, user=request.user),
                                                'isThisUser': False})

@csrf_exempt
@login_required()
def ajax_get_post(request, postNumber):
    if request.is_ajax():
        followingUsers = MyUser.objects.get(user=request.user).followingUsers.all()
        posts = Post.objects.filter(user=followingUsers).order_by('-pubDate')[int(postNumber)+1: int(postNumber)+2]

        tmp = serializers.serialize('json', list(posts), use_natural_foreign_keys=True, use_natural_primary_keys=True)
        return HttpResponse(tmp)

@csrf_exempt
@login_required()
def ajax_get_comments(request, postID):
    if request.is_ajax():
        tmp = serializers.serialize('json', list(Post.objects.get(id=postID).comment_set.all().order_by('-id')),
                                    use_natural_foreign_keys=True, use_natural_primary_keys=True)
        return HttpResponse(tmp)


@csrf_exempt
def ajax_comment_on_post(request, postID):
    if request.is_ajax():
        post = get_object_or_404(Post, id=postID)
        comment = Comment()
        comment.user = get_object_or_404(MyUser, user=request.user)
        comment.post = post
        comment.body = json.loads(request.read().decode('utf-8'))['comment']
        comment.save()

        return HttpResponse(serializers.serialize('json', [comment],
                                                  use_natural_foreign_keys=True, use_natural_primary_keys=True))