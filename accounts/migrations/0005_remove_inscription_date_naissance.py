# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20160225_1323'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inscription',
            name='date_naissance',
        ),
    ]
