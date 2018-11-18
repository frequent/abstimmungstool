# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-12 20:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('initproc', '0039_auto_20181111_1013'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='policy',
            options={'permissions': [('policy_create', 'Can create new policy'), ('policy_edit', 'Can edit policy'), ('policy_delete', 'Can delete policy'), ('policy_submit', 'Can submit policy'), ('policy_invite', 'Can invite others to co-initiate/support'), ('policy_stage', 'Can stage a policy'), ('policy_validate', 'Can validate a policy'), ('policy_invalidate', 'Can invalidate a policy'), ('policy_finalise', 'Can finalise a policy'), ('policy_discuss', 'Can move a policy into discussion'), ('policy_review', 'Can move a policy into final review'), ('policy_release', 'Can release a policy for a vote')]},
        ),
        migrations.AlterField(
            model_name='policy',
            name='state',
            field=models.CharField(choices=[('draft', 'in preparation'), ('deleted', 'deleted'), ('staged', 'staged'), ('submitted', 'submitted'), ('invalidated', 'invalidated'), ('rejected', 'rejected'), ('closed', 'closed'), ('hidden', 'hidden'), ('challenged', 'challenged'), ('validated', 'validated'), ('supported', 'supported'), ('finalised', 'finalised'), ('discussed', 'in discussion'), ('reviewed', 'in review'), ('released', 'released'), ('voted', 'put to vote')], default='draft', max_length=20),
        ),
    ]