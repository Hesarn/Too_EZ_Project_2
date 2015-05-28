# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20150527_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='likeUsers',
            field=models.ManyToManyField(blank=True, related_name='like', to='users.MyUser'),
        ),
    ]
