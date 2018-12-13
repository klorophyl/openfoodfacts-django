# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('off_django', '0009_offpackaging_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='offfood',
            name='nova_group',
            field=models.IntegerField(null=True, default=None),
        ),
    ]
