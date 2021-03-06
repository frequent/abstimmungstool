# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-27 16:41
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Argument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('changed_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=80)),
                ('text', models.TextField()),
                ('in_favor', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('changed_at', models.DateTimeField(auto_now=True)),
                ('text', models.TextField()),
                ('argument', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='initproc.Argument')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Initiative',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('state', models.CharField(choices=[('i', 'new arrivals'), ('s', 'seeking support'), ('d', 'in discussion'), ('e', 'final edits'), ('m', 'with moderation team'), ('h', 'hidden'), ('v', 'is being voted on'), ('a', 'was accepted'), ('r', 'was rejected')], max_length=1)),
                ('quorum', models.IntegerField(default=30)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('changed_at', models.DateTimeField(auto_now=True)),
                ('summary', models.TextField()),
                ('forderung', models.TextField()),
                ('kosten', models.TextField()),
                ('fin_vorschlag', models.TextField()),
                ('arbeitsweise', models.TextField()),
                ('init_argument', models.TextField()),
                ('einordnung', models.CharField(max_length=50)),
                ('ebene', models.CharField(max_length=50)),
                ('bereich', models.CharField(max_length=50)),
                ('went_to_discussion_at', models.DateTimeField(blank=True, null=True)),
                ('went_to_voting_at', models.DateTimeField(blank=True, null=True)),
                ('was_closed_at', models.DateTimeField(blank=True, null=True)),
                ('initiators', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('argument', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='initproc.Argument')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Supporter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('public', models.BooleanField(default=True)),
                ('initiative', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='supporters', to='initproc.Initiative')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('changed_at', models.DateTimeField(auto_now=True)),
                ('in_favor', models.BooleanField(default=True)),
                ('initiative', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='votes', to='initproc.Initiative')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='argument',
            name='initiative',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arguments', to='initproc.Initiative'),
        ),
        migrations.AddField(
            model_name='argument',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='vote',
            unique_together=set([('user', 'initiative')]),
        ),
        migrations.AlterUniqueTogether(
            name='supporter',
            unique_together=set([('user', 'initiative')]),
        ),
        migrations.AlterUniqueTogether(
            name='like',
            unique_together=set([('user', 'argument')]),
        ),
    ]
