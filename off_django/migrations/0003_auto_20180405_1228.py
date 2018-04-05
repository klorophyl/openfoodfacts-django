# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('off_django', '0002_offfood_serving_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='offfood',
            name='image_ingredients_small_url',
            field=models.TextField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='offfood',
            name='image_ingredients_url',
            field=models.TextField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='offfood',
            name='image_nutrition_small_url',
            field=models.TextField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='offfood',
            name='image_nutrition_url',
            field=models.TextField(default=None, null=True),
        ),
    ]
