# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import off_django.models_extensions


class Migration(migrations.Migration):

    dependencies = [
        ('off_django', '0007_offbrand'),
    ]

    operations = [
        migrations.CreateModel(
            name='OFFCategory',
            fields=[
                ('facet_id', models.CharField(max_length=255, serialize=False, primary_key=True, db_index=True)),
                ('name_fr', models.TextField(default=None, null=True)),
                ('name_en', models.TextField(default=None, null=True)),
                ('products', models.IntegerField(default=None, null=True)),
                ('url', models.TextField(default=None, null=True)),
                ('same_as', off_django.models_extensions.ListField(default=None, null=True)),
            ],
            options={
                'verbose_name': 'OFFCategory - Model for Open Food Facts facet category',
            },
        ),
        migrations.CreateModel(
            name='OFFCountry',
            fields=[
                ('facet_id', models.CharField(max_length=255, serialize=False, primary_key=True, db_index=True)),
                ('name_fr', models.TextField(default=None, null=True)),
                ('name_en', models.TextField(default=None, null=True)),
                ('products', models.IntegerField(default=None, null=True)),
                ('url', models.TextField(default=None, null=True)),
                ('same_as', off_django.models_extensions.ListField(default=None, null=True)),
            ],
            options={
                'verbose_name': 'OFFCountry - Model for Open Food Facts facet country',
            },
        ),
        migrations.CreateModel(
            name='OFFIngredient',
            fields=[
                ('facet_id', models.CharField(max_length=255, serialize=False, primary_key=True, db_index=True)),
                ('name_fr', models.TextField(default=None, null=True)),
                ('name_en', models.TextField(default=None, null=True)),
                ('products', models.IntegerField(default=None, null=True)),
                ('url', models.TextField(default=None, null=True)),
                ('same_as', off_django.models_extensions.ListField(default=None, null=True)),
            ],
            options={
                'verbose_name': 'OFFIngredient - Model for Open Food Facts facet ingredient',
            },
        ),
        migrations.CreateModel(
            name='OFFLanguage',
            fields=[
                ('facet_id', models.CharField(max_length=255, serialize=False, primary_key=True, db_index=True)),
                ('name_fr', models.TextField(default=None, null=True)),
                ('name_en', models.TextField(default=None, null=True)),
                ('products', models.IntegerField(default=None, null=True)),
                ('url', models.TextField(default=None, null=True)),
                ('same_as', off_django.models_extensions.ListField(default=None, null=True)),
            ],
            options={
                'verbose_name': 'OFFLanguage - Model for Open Food Facts facet language',
            },
        ),
        migrations.CreateModel(
            name='OFFPackaging',
            fields=[
                ('facet_id', models.CharField(max_length=255, serialize=False, primary_key=True, db_index=True)),
                ('name_fr', models.TextField(default=None, null=True)),
                ('name_en', models.TextField(default=None, null=True)),
                ('products', models.IntegerField(default=None, null=True)),
                ('url', models.TextField(default=None, null=True)),
                ('same_as', off_django.models_extensions.ListField(default=None, null=True)),
            ],
            options={
                'verbose_name': 'OFFPackaging - Model for Open Food Facts facet packaging',
            },
        ),
        migrations.CreateModel(
            name='OFFPackagingCode',
            fields=[
                ('facet_id', models.CharField(max_length=255, serialize=False, primary_key=True, db_index=True)),
                ('name_fr', models.TextField(default=None, null=True)),
                ('name_en', models.TextField(default=None, null=True)),
                ('products', models.IntegerField(default=None, null=True)),
                ('url', models.TextField(default=None, null=True)),
                ('same_as', off_django.models_extensions.ListField(default=None, null=True)),
            ],
            options={
                'verbose_name': 'OFFPackagingCode - Model for Open Food Facts facet packaging code',
            },
        ),
        migrations.CreateModel(
            name='OFFPurchasePlace',
            fields=[
                ('facet_id', models.CharField(max_length=255, serialize=False, primary_key=True, db_index=True)),
                ('name_fr', models.TextField(default=None, null=True)),
                ('name_en', models.TextField(default=None, null=True)),
                ('products', models.IntegerField(default=None, null=True)),
                ('url', models.TextField(default=None, null=True)),
                ('same_as', off_django.models_extensions.ListField(default=None, null=True)),
            ],
            options={
                'verbose_name': 'OFFPurchasePlace - Model for Open Food Facts facet purchase place',
            },
        ),
        migrations.CreateModel(
            name='OFFState',
            fields=[
                ('facet_id', models.CharField(max_length=255, serialize=False, primary_key=True, db_index=True)),
                ('name_fr', models.TextField(default=None, null=True)),
                ('name_en', models.TextField(default=None, null=True)),
                ('products', models.IntegerField(default=None, null=True)),
                ('url', models.TextField(default=None, null=True)),
                ('same_as', off_django.models_extensions.ListField(default=None, null=True)),
            ],
            options={
                'verbose_name': 'OFFState - Model for Open Food Facts facet state',
            },
        ),
        migrations.CreateModel(
            name='OFFStore',
            fields=[
                ('facet_id', models.CharField(max_length=255, serialize=False, primary_key=True, db_index=True)),
                ('name_fr', models.TextField(default=None, null=True)),
                ('name_en', models.TextField(default=None, null=True)),
                ('products', models.IntegerField(default=None, null=True)),
                ('url', models.TextField(default=None, null=True)),
                ('same_as', off_django.models_extensions.ListField(default=None, null=True)),
            ],
            options={
                'verbose_name': 'OFFStore - Model for Open Food Facts facet store',
            },
        ),
        migrations.CreateModel(
            name='OFFTrace',
            fields=[
                ('facet_id', models.CharField(max_length=255, serialize=False, primary_key=True, db_index=True)),
                ('name_fr', models.TextField(default=None, null=True)),
                ('name_en', models.TextField(default=None, null=True)),
                ('products', models.IntegerField(default=None, null=True)),
                ('url', models.TextField(default=None, null=True)),
                ('same_as', off_django.models_extensions.ListField(default=None, null=True)),
            ],
            options={
                'verbose_name': 'OFFTrace - Model for Open Food Facts facet trace',
            },
        ),
    ]
