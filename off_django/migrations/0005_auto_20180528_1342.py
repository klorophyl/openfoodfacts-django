# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('off_django', '0004_offadditive'),
    ]

    operations = [
        migrations.CreateModel(
            name='OFFAllergen',
            fields=[
                ('facet_id', models.CharField(max_length=255, serialize=False, primary_key=True, db_index=True)),
                ('name_fr', models.TextField(default=None, null=True)),
                ('name_en', models.TextField(default=None, null=True)),
                ('products', models.IntegerField(default=None, null=True)),
                ('url', models.TextField(default=None, null=True)),
            ],
            options={
                'verbose_name': 'OFFAllergen - Model for Open Food Facts facet allergen',
            },
        ),
        migrations.AlterModelOptions(
            name='offadditive',
            options={'verbose_name': 'OFFAdditive - Model for Open Food Facts facet additive'},
        ),
    ]
