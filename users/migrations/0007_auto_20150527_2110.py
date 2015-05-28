# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20150526_1932'),
    ]

    operations = [
        migrations.CreateModel(
            name='CastFilm',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('roleName', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('picture', models.ImageField(upload_to='', default='/static/img/user.png')),
                ('description', models.TextField()),
                ('averageScore', models.IntegerField(default=0)),
                ('imdbLink', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='myuser',
            name='birthday',
            field=models.CharField(default='-1', max_length=10),
        ),
        migrations.AlterField(
            model_name='post',
            name='film_name',
            field=models.ForeignKey(to='users.Film'),
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
            model_name='castfilm',
            name='film',
            field=models.ForeignKey(to='users.Film'),
        ),
    ]
