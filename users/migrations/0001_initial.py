# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import datetime


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('profilePicture', models.ImageField(default='/static/img/user.png', upload_to='')),
                ('followerUsers', models.ManyToManyField(to='users.MyUser', related_name='followerUsers_rel_+', blank=True)),
                ('followingUsers', models.ManyToManyField(to='users.MyUser', related_name='followingUsers_rel_+', blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('film_name', models.CharField(max_length=50)),
                ('score', models.IntegerField()),
                ('body', models.TextField()),
                ('pub_date', models.DateTimeField(default=datetime.datetime.now)),
                ('user', models.ForeignKey(to='users.MyUser')),
            ],
        ),
    ]
