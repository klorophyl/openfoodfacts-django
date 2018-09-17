#!/usr/bin/python
# -*- coding: utf-8 -*-

import csv
import logging
import os
import sys
import time

from tqdm import tqdm

from .utils import download_file, get_off_model

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

        dump_file = download_file(self.DUMP_URL, "dump.csv")

        logger.info("[openfoodfacts] - Dump downloaded in %ss" % int(time.time() - timestamp))

        return dump_file

    def get_csv_reader(self, dump_file):
        """
        Parse a dump file and return a csv reader enumerator
        """
        return csv.DictReader(dump_file, delimiter="\t")

    def load_dump(self):
        """
        Download, parse and load latest dump in DB
        //!\\  ignore products with no 'code'
        """

        csv.field_size_limit(sys.maxsize)  # Necessary because OFF DB is so big

        all_count = 0
        new_count = 0
        upd_count = 0

        # Download CSV
        try:
            dump_path = self.download_dump()
        except Exception as e:
            logger.error(e)
            logger.error("[openfoodfacts] - An error occurred during dump download")
            return

        with open(dump_path, "r") as dump_file:
            dump_file.seek(0)

            model = get_off_model()

            # Preload last_modified values
            last_modified_map = dict(model.objects.all().values_list("code", "last_modified_t"))

            # Parse CSV
            for entry in self.get_csv_reader(dump_file):
                code = entry.get("code", "")
                if code == "":
                    continue

                all_count += 1

                saved_last_modified = last_modified_map.get(code)
                if saved_last_modified is None:
                    model.load(entry, create=True)
                    new_count += 1
                elif int(entry.get("last_modified_t")) > saved_last_modified:
                    model.load(entry)
                    upd_count += 1

                if all_count != 0 and all_count % 50000 == 0:
                    logger.info("[openfoodfacts] - %s products parsed, %s created, %s updated" % (all_count, new_count, upd_count))

        os.remove(dump_path)
        logger.info("[openfoodfacts] - load_dump done")
