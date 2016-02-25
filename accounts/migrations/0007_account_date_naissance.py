# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_delete_inscription'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='date_naissance',
            field=models.DateField(default=datetime.datetime(2016, 2, 25, 16, 2, 1, 796808, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
