# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-19 17:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_auto_20160319_1249'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='question_text',
            new_name='city_text',
        ),
        migrations.RemoveField(
            model_name='question',
            name='pub_date',
        ),
        migrations.AddField(
            model_name='temperature',
            name='temperature',
            field=models.ForeignKey(default=20, on_delete=django.db.models.deletion.CASCADE, to='polls.Question'),
            preserve_default=False,
        ),
    ]