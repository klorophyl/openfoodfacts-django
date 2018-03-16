#!/usr/bin/python
# -*- coding: utf-8 -*-

import math
import requests

from StringIO import StringIO
from tqdm import tqdm

DATETIME_FORMAT = "%Y-%m-%dT%H:%M:%SZ"


def download_file(url):
    """
    Download a file into a StringIO object
    """
    response = requests.get(url, stream=True)

    block_size = 1024
    total_size = int(response.headers.get('content-length', 0))

    outfile = StringIO()

    iterator = tqdm(response.iter_content(block_size), total=math.ceil(total_size // block_size), unit='KB', unit_scale=True)
    for chunk in iterator:
        outfile.write(chunk)

    return outfile
