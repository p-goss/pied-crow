# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-04 20:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BellSchedule', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NormalScheduleRotation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField()),
                ('schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BellSchedule.Schedule')),
            ],
        ),
        migrations.CreateModel(
            name='SpecialDays',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('keep_normal_rotation', models.BooleanField(default=False, verbose_name='Saturday Off')),
                ('schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BellSchedule.Schedule')),
            ],
        ),
        migrations.CreateModel(
            name='YearCalendar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Schedule Name')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('sun_off', models.BooleanField(default=True, verbose_name='Sunday Off')),
                ('mon_off', models.BooleanField(default=False, verbose_name='Monday Off')),
                ('tue_off', models.BooleanField(default=False, verbose_name='Tuesday Off')),
                ('wed_off', models.BooleanField(default=False, verbose_name='Wednesday Off')),
                ('thr_off', models.BooleanField(default=False, verbose_name='Thursday Off')),
                ('fri_off', models.BooleanField(default=False, verbose_name='Friday Off')),
                ('sat_off', models.BooleanField(default=True, verbose_name='Saturday Off')),
            ],
        ),
        migrations.AlterField(
            model_name='ringpatternpart',
            name='on_off',
            field=models.BooleanField(verbose_name='On'),
        ),
        migrations.AddField(
            model_name='specialdays',
            name='year_calendar',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BellSchedule.YearCalendar'),
        ),
        migrations.AddField(
            model_name='normalschedulerotation',
            name='year_calendar',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BellSchedule.YearCalendar'),
        ),
    ]