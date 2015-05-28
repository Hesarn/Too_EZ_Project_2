# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0023_notification'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='description',
        ),
        migrations.AddField(
            model_name='notification',
            name='notificationPost',
            field=models.ForeignKey(blank=True, null=True, to='users.Post'),
        ),
        migrations.AddField(
            model_name='notification',
            name='notificationState',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
