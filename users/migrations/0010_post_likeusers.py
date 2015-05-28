# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20150527_2121'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likeUsers',
            field=models.ManyToManyField(related_name='like', to='users.MyUser'),
        ),
    ]
