# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-03-25 15:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course_metadata', '0163_drop_draft_unique_video_image_person'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='draft',
        ),
        migrations.RemoveField(
            model_name='person',
            name='draft',
        ),
        migrations.RemoveField(
            model_name='video',
            name='draft',
        ),
    ]