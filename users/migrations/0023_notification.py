# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0022_auto_20150528_1221'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('description', models.CharField(max_length=300)),
                ('firstUser', models.ForeignKey(related_name='first', to='users.MyUser')),
                ('secondUser', models.ForeignKey(related_name='second', to='users.MyUser')),
            ],
        ),
    ]
