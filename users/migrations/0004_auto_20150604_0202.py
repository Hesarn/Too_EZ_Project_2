# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20150603_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='likeUsers',
            field=models.ManyToManyField(related_name='like', default=(), to='users.MyUser'),
        ),
    ]
