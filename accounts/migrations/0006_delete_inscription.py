# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_remove_inscription_date_naissance'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Inscription',
        ),
    ]
