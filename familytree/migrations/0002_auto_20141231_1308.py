# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('familytree', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='parent',
        ),
        migrations.AddField(
            model_name='person',
            name='parents',
            field=models.ManyToManyField(related_name='p', null=True, verbose_name=b'Parents', to='familytree.Person', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='children',
            field=models.ManyToManyField(related_name='c', null=True, verbose_name=b'Children', to='familytree.Person', blank=True),
            preserve_default=True,
        ),
    ]
