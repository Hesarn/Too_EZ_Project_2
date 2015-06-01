from django.shortcuts import render, get_object_or_404
from users.forms import loginForm, signupForm
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from users.models import Film
from django import forms
from users.models import MyUser, Post, Comment, Notification
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
                                         'posts': Post.objects.filter(id=postID)})


@login_required()
def show_user_profile(request):
    reqUser = get_object_or_404(MyUser, user=request.user)
    return render(request, 'userProfile.html', {'user': reqUser,
                                                'currUser': get_object_or_404(MyUser, user=request.user),
                                                'posts': Post.objects.filter(user=reqUser),
                                                'isThisUser': True})

@login_required()
def show_other_profiles(request, userID):
    if get_object_or_404(MyUser, user=request.user) == get_object_or_404(MyUser, id=userID):
        return show_user_profile(request)

    else:
        reqUser = get_object_or_404(MyUser, id=userID)
        return render(request, 'userProfile.html', {'user': get_object_or_404(MyUser, id=userID),
                                                    'currUser': get_object_or_404(MyUser, user=request.user),
                                                    'posts': Post.objects.filter(user=reqUser)})

@csrf_exempt
@login_required()
def ajax_get_post(request, postNumber):
    if request.is_ajax():
        followingUsers = MyUser.objects.get(user=request.user).followingUsers.all()
        post = Post.objects.filter(user=followingUsers).order_by('-pubDate')[int(postNumber)]

        return HttpResponse(render(request, 'post_AJAX.html', {'user': post.user,
                                                               'currUser': get_object_or_404(MyUser, user=request.user),
                                                               'post': post}))


@csrf_exempt
def ajax_comment_on_post(request, postID):
    post = get_object_or_404(Post, id=postID)

    if request.is_ajax():
        tmpUsers = set()

        for cm in post.comment_set.all():
            tmpUsers.add(cm.user)

        for user in tmpUsers:
            if user != get_object_or_404(Post, id=postID).user and user.user != request.user:
                addNotification(request, user, postID, 4, True)

        comment = Comment()
        comment.user = get_object_or_404(MyUser, user=request.user)
        comment.post = post
        comment.body = json.loads(request.read().decode('utf-8'))['comment']
        comment.save()

        if request.user != get_object_or_404(Post, id=postID).user.user:
            addNotification(request, get_object_or_404(Post, id=postID).user, postID, 2, True)

        return render(request, 'comment_AJAX.html', {'cm': comment})

@csrf_exempt
def ajax_like_post(request, postID):
    if request.is_ajax():
        post = get_object_or_404(Post, id=postID)
        currUser = get_object_or_404(MyUser, user=request.user)

        if post.likeUsers.filter(user=currUser.user).count() == 0:
            if currUser != post.user:
                addNotification(request, get_object_or_404(Post, id=postID).user, postID, 1, True)
            post.likeUsers.add(currUser)
            return HttpResponse('Post successfully Liked !')

        else:
            addNotification(request, get_object_or_404(Post, id=postID).user, postID, 1, False)
            post.likeUsers.remove(currUser)
            return HttpResponse('unliked !')

def show_users(request, follow, userID):
    if follow == 'following':
        return render(request, 'person.html', {'users': get_object_or_404(MyUser, id=userID).followingUsers.all(),
                                               'currUser': get_object_or_404(MyUser, user=request.user)})

    elif follow == 'follower':
        return render(request, 'person.html', {'users': get_object_or_404(MyUser, id=userID).followerUsers.all(),
                                               'currUser': get_object_or_404(MyUser, user=request.user)})

@csrf_exempt
def follow_action(request, userID):
    currUser = get_object_or_404(MyUser, user=request.user)
    tmpUser = get_object_or_404(MyUser, id=userID)

    if tmpUser not in currUser.followingUsers.all():
        addNotification(request, tmpUser, None, 3, True)
        currUser.followingUsers.add(tmpUser)
        tmpUser.followerUsers.add(currUser)

        return HttpResponse('successfully follow user')

    else:
        addNotification(request, tmpUser, None, 3, False)
        currUser.followingUsers.remove(tmpUser)
        tmpUser.followerUsers.remove(currUser)

        return HttpResponse('successfully unfollow user')


def addNotification(request, secondUser, postID, notificationState, isAdd):
    post = None

    try:
        post = get_object_or_404(Post, id=postID)
    except:
        pass

    currUser = get_object_or_404(MyUser, user=request.user)
    tmpUser = secondUser

    notification = Notification()
    notification.firstUser = currUser
    notification.secondUser = tmpUser
    notification.post = post
    notification.notificationState = notificationState

    if isAdd:
        currUser.first.add(notification)
        tmpUser.second.add(notification)

    else:
        Notification.objects.filter(firstUser=notification.firstUser).filter(secondUser=notification.secondUser) \
                                        .filter(post=notification.post) \
                                        .filter(notificationState=notification.notificationState).delete()

