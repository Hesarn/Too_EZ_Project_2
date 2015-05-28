# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20150527_2110'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='film_name',
            new_name='filmName',
        ),
    ]
