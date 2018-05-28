#!/usr/bin/python
# -*- coding: utf-8 -*-

import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tests.settings")
django.setup()
