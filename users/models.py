from django.db import models
from django.contrib.auth.models import User
import datetime
from Project2.settings import STATIC_URL

class MyUser(models.Model):
    user = models.OneToOneField(User)
    birthday = models.CharField(max_length=10, default='-1')
    followingUsers = models.ManyToManyField('self', blank=True)
    followerUsers = models.ManyToManyField('self', blank=True)
    profilePicture = models.ImageField(default=(STATIC_URL + 'img/user.png'))

    def __str__(self):
        return self.user.first_name


class Film(models.Model):
    name = models.CharField(max_length=50)
    picture = models.ImageField(default=(STATIC_URL + 'img/user.png'))
    description = models.TextField()
    averageScore = models.IntegerField(default=0)
    imdbLink = models.CharField(max_length=200)
    profileLink = models.CharField(max_length=200, default='movieProfile.html')

    def __str__(self):
        return self.name


class Cast(models.Model):
    name = models.CharField(max_length=100)
    roleName = models.CharField(max_length=100)
    film = models.ForeignKey(Film)

    def __str__(self):
        return self.name


class Post(models.Model):
    user = models.ForeignKey(MyUser)
    film = models.ForeignKey(Film)
    score = models.IntegerField()
    body = models.TextField()
    pubDate = models.DateTimeField(default=datetime.datetime.now)
    likeUsers = models.ManyToManyField(MyUser, related_name='like', blank=True)

    def __str__(self):
        return self.user.user.username + ' posted about ' + self.film.name


class Comment(models.Model):
    user = models.ForeignKey(MyUser)
    post = models.ForeignKey(Post)
    body = models.TextField()

    def __str__(self):
        return self.user.user.first_name + ' commented on ' + self.post.user.user.username + "'s post"


class Notification(models.Model):
    firstUser = models.ForeignKey(MyUser, related_name='first')
    secondUser = models.ForeignKey(MyUser, related_name='second')
    notificationPost = models.ForeignKey(Post, blank=True, null=True)
    notificationState = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.firstUser.user.username + ' to ' + self.secondUser.user.username