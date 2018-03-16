#!/usr/bin/python
# -*- coding: utf-8 -*-

import csv
import logging
import sys
import time

from tqdm import tqdm

from django.conf import settings
from django.db.models.loading import get_model

from .models import OFFFood
from .utils import download_file

logger = logging.getLogger("django")


class DumpManager(object):
    """
    Manage Open Food Facts dumps download / load in database.
    Use CSV API
    """

    DUMP_URL = "https://world.openfoodfacts.org/data/en.openfoodfacts.org.products.csv"

    def download_dump(self):
        """
        Download dump from Open Food Facts service
        """
        logger.info("[openfoodfacts] - Starting dump download...")
        timestamp = time.time()

        dump_file = download_file(self.DUMP_URL)

        logger.info("[openfoodfacts] - Dump downloaded in %s" % (time.time() - timestamp))

        return dump_file

    def get_csv_reader(self, dump_file):
        """
        Parse a dump file and return a csv reader enumerator
        """
        return csv.DictReader(dump_file, delimiter="\t")

    def load_dump(self):
        """
        Download, parse and load latest dump in DB
        /!\ ignore products with no 'code'
        """

        csv.field_size_limit(sys.maxsize)  # Necessary because OFF DB is so big

        # Download CSV
        try:
            dump_file = self.download_dump()
        except Exception as e:
            logger.error(e)
            logger.error("[openfoodfacts] - An error occurred, please check that you have at least 2Go of RAM available")

        entry_count = dump_file.read().count("\n")
        dump_file.seek(0)

        # Load custom model if it exists
        model = OFFFood
        if hasattr(settings, "OFF_MODEL"):
            splitted = settings.OFF_MODEL.split(".")
            model = get_model(".".join(splitted[:-1]), splitted[-1])

        # Preload last_modified values
        last_modified_map = dict(model.objects.all().values_list("code", "last_modified_t"))

        # Parse CSV
        reader = self.get_csv_reader(dump_file)
        iterator = tqdm(reader, total=entry_count, unit='it', unit_scale=True)
        for entry in iterator:
            code = entry.get("code", "")
            if code == "":
                continue

            saved_last_modified = last_modified_map.get(code)
            if saved_last_modified is None:
                model.load(entry, create=True)
            elif int(entry.get("last_modified_t")) > saved_last_modified:
                model.load(entry)

        dump_file.close()
