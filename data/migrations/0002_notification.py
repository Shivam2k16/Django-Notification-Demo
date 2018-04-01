# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('truck_number', models.CharField(max_length=10)),
                ('insurance_date', models.DateField()),
                ('fitness_date', models.DateField()),
                ('pollution_date', models.DateField()),
                ('remaining_insurance', models.DateField()),
                ('remaining_fitness', models.DateField()),
                ('remaining_pollution', models.DateField()),
                ('remainder', models.IntegerField(default=31)),
                ('read', models.BooleanField(default=False)),
                ('remainded_day_insurane', models.IntegerField(default=31)),
                ('remainded_day_fitness', models.IntegerField(default=31)),
                ('remainded_day_pollution', models.IntegerField(default=31)),
            ],
        ),
    ]
