# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0021_auto_20150528_1153'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CastFilm',
            new_name='Cast',
        ),
    ]
