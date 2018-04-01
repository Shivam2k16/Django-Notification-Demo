# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_notification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='remaining_fitness',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='notification',
            name='remaining_insurance',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='notification',
            name='remaining_pollution',
            field=models.IntegerField(),
        ),
    ]
