# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_post_likeusers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='likeUsers',
            field=models.ManyToManyField(default=None, to='users.MyUser', related_name='like'),
        ),
    ]
