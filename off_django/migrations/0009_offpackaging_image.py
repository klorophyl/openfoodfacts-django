# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('off_django', '0008_offcategory_offcountry_offingredient_offlanguage_offpackaging_offpackagingcode_offpurchaseplace_offs'),
    ]

    operations = [
        migrations.AddField(
            model_name='offpackaging',
            name='image',
            field=models.TextField(default=None, null=True),
        ),
    ]
