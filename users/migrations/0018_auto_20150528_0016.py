# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_auto_20150528_0006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='profilePicture',
            field=models.ImageField(upload_to='/films', default='/static/img/user.png'),
        ),
    ]
