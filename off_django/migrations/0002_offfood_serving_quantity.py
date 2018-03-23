# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('off_django', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='offfood',
            name='serving_quantity',
            field=models.FloatField(default=None, null=True),
        ),
    ]
