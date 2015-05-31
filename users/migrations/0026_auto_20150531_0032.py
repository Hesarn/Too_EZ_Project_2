# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0025_auto_20150531_0030'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='profilePicture_height',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='profilePicture_width',
        ),
    ]
