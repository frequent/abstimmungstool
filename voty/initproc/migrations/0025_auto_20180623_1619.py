# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-06-23 14:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('initproc', '0024_merge_20180510_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='initiative',
            name='bereich',
            field=models.CharField(choices=[('Global Politics & International Cooperation', 'Global Politics & International Cooperation'), ('Education, Research & Culture', 'Education, Research & Culture'), ('Interior Politics', 'Interior Politics'), ('Net- & Media Politics', 'Net- & Media Politics'), ('Gender Equality', 'Gender Equality'), ('Diversity & Integration', 'Diversity & Integration'), ('Democracy & Transparency', 'Democracy & Transparency'), ('Health, Nutrition, Consumer Protection', 'Health, Nutrition, Consumer Protection'), ('Environment, Mobility, Infrastructural Development', 'Environment, Mobility, Infrastructural Development'), ('Social Justice, Economy, Work & Finance', 'Social Justice, Economy, Work & Finance'), ('Other', 'Other')], max_length=50),
        ),
        migrations.AlterField(
            model_name='initiative',
            name='ebene',
            field=models.CharField(choices=[('Federal Level', 'Federal Level')], max_length=50),
        ),
        migrations.AlterField(
            model_name='initiative',
            name='einordnung',
            field=models.CharField(choices=[('Single Initiative', 'Single Initiative')], max_length=50),
        ),
    ]