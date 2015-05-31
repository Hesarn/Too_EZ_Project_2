# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0024_auto_20150528_1920'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='profilePicture_height',
            field=models.PositiveIntegerField(editable=False, default='100', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='myuser',
            name='profilePicture_width',
            field=models.PositiveIntegerField(editable=False, default='100', null=True, blank=True),
        ),
    ]
