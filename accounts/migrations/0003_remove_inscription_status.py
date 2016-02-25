# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_inscription'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inscription',
            name='status',
        ),
    ]
