# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_auto_20150527_2151'),
    ]

    operations = [
        migrations.RenameField(
            model_name='film',
            old_name='filmLink',
            new_name='profileLink',
        ),
    ]
