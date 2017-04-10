# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-07 19:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SavedUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=16)),
                ('handle', models.CharField(max_length=100, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('influencer', models.CharField(max_length=16)),
                ('followers', models.IntegerField()),
                ('following', models.IntegerField()),
                ('description', models.TextField()),
            ],
        ),
    ]