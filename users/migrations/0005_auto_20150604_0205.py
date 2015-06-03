# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20150604_0202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='likeUsers',
            field=models.ManyToManyField(related_name='like', blank=True, to='users.MyUser'),
        ),
    ]
