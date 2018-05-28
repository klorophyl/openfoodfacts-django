# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import off_django.models_extensions


class Migration(migrations.Migration):

    dependencies = [
        ('off_django', '0006_offallergen_same_as'),
    ]

    operations = [
        migrations.CreateModel(
            name='OFFBrand',
            fields=[
                ('facet_id', models.CharField(max_length=255, serialize=False, primary_key=True, db_index=True)),
                ('name_fr', models.TextField(default=None, null=True)),
                ('name_en', models.TextField(default=None, null=True)),
                ('products', models.IntegerField(default=None, null=True)),
                ('url', models.TextField(default=None, null=True)),
                ('same_as', off_django.models_extensions.ListField(default=None, null=True)),
            ],
            options={
                'verbose_name': 'OFFBrand - Model for Open Food Facts facet band',
            },
        ),
    ]
