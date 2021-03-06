# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-20 07:46
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0009_auto_20171020_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='img_profile',
            field=models.ImageField(blank=True, default='/media/default-profile.jpg', upload_to='user', verbose_name='프로필 사진'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user',
            field=models.ManyToManyField(blank=True, related_name='following_user', to=settings.AUTH_USER_MODEL, verbose_name='팔로우 유저'),
        ),
    ]
