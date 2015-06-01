# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cast',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('roleName', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('body', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('picture', models.ImageField(upload_to='', default='/static/img/user.png')),
                ('description', models.TextField()),
                ('averageScore', models.IntegerField(default=0)),
                ('imdbLink', models.CharField(max_length=200)),
                ('profileLink', models.CharField(max_length=200, default='movieProfile.html')),
            ],
        ),
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('birthday', models.CharField(max_length=10, default='-1')),
                ('profilePicture', models.ImageField(upload_to='', default='/static/img/user.png')),
                ('followerUsers', models.ManyToManyField(to='users.MyUser', blank=True)),
                ('followingUsers', models.ManyToManyField(to='users.MyUser', blank=True, related_name='following')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('notificationState', models.IntegerField(blank=True, null=True)),
                ('firstUser', models.ForeignKey(to='users.MyUser', related_name='first')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('score', models.IntegerField()),
                ('body', models.TextField()),
                ('pubDate', models.DateTimeField(default=datetime.datetime.now)),
                ('film', models.ForeignKey(to='users.Film')),
                ('likeUsers', models.ManyToManyField(to='users.MyUser', blank=True, related_name='like')),
                ('user', models.ForeignKey(to='users.MyUser')),
            ],
        ),
        migrations.AddField(
            model_name='notification',
            name='notificationPost',
            field=models.ForeignKey(to='users.Post', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='notification',
            name='secondUser',
            field=models.ForeignKey(to='users.MyUser', related_name='second'),
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(to='users.Post'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(to='users.MyUser'),
        ),
        migrations.AddField(
            model_name='cast',
            name='film',
            field=models.ForeignKey(to='users.Film'),
        ),
    ]
