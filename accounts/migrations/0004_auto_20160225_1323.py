# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_remove_inscription_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscription',
            name='date_inscription',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='inscription',
            name='date_naissance',
            field=models.DateField(),
        ),
    ]
