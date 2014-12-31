# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('sex', models.CharField(max_length=1, choices=[(b'M', b'Male'), (b'F', b'Female')])),
                ('children', models.ManyToManyField(related_name='children_rel_+', null=True, verbose_name=b'Children', to='familytree.Person', blank=True)),
                ('parent', models.ManyToManyField(related_name='parent_rel_+', null=True, verbose_name=b'Parent', to='familytree.Person', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
