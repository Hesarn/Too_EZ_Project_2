# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_auto_20150527_2143'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='filmName',
            new_name='film',
        ),
        migrations.AddField(
            model_name='film',
            name='filmLink',
            field=models.CharField(default='movieProfile.html', max_length=200),
        ),
    ]
