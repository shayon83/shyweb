# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-07-02 04:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fileapi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='files',
            name='file_attach',
            field=models.BinaryField(default=b''),
        ),
    ]
