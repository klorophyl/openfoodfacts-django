# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import off_django.models_extensions


class Migration(migrations.Migration):

    dependencies = [
        ('off_django', '0005_auto_20180528_1342'),
    ]

    operations = [
        migrations.AddField(
            model_name='offallergen',
            name='same_as',
            field=off_django.models_extensions.ListField(default=None, null=True),
        ),
    ]
