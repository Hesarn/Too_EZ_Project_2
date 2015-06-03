# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20150604_0205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='averageScore',
            field=models.FloatField(default=0),
        ),
    ]
