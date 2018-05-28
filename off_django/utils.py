#!/usr/bin/python
# -*- coding: utf-8 -*-

import math
import os
import requests

from tqdm import tqdm

from django.apps import apps
from django.conf import settings

from .models import OFFFood


def download_file(url, filename):
    """
    Download a file into a StringIO object
    """
    response = requests.get(url, stream=True)

    block_size = 1024
    total_size = int(response.headers.get('content-length', 0))

    path = os.path.join(settings.OFF_TMP_FOLDER_PATH, filename)
    with open(path, "w") as outfile:
        iterator = tqdm(response.iter_content(block_size), total=math.ceil(total_size // block_size), unit='KB', unit_scale=True)
        for chunk in iterator:
            outfile.write(chunk)

    return path


def get_off_model():
    """
    Returns custom OFF model if it exists, else take defaul off_django OFFFood
    """

    model = OFFFood
    if hasattr(settings, "OFF_MODEL"):
        splitted = settings.OFF_MODEL.split(".")
        model = apps.get_model(".".join(splitted[:-1]), splitted[-1])

    return model
