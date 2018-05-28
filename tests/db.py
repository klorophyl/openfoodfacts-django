#!/usr/bin/python
# -*- coding: utf-8 -*-

import mock
import os
import unittest

from off_django.db import DumpManager


class TestDumpManager(unittest.TestCase):

    def setUp(self):
        self.manager = DumpManager()

    @mock.patch("off_django.db.download_file")
    def test_download_dump(self, mock_download_file):
        return_value = "foo/bar"
        mock_download_file.return_value = return_value

        path = self.manager.download_dump()

        self.assertEqual(path, return_value)

    @mock.patch("off_django.db.csv.DictReader")
    def test_get_csv_reader(self, mock_dict_reader):
        file = "foo"

        self.manager.get_csv_reader(file)
        mock_dict_reader.assert_called_with(file, delimiter="\t")

    def test_load_dump(self):
        self.manager.download_dump = mock.MagicMock()
        self.manager.download_dump.side_effect = Exception()

        self.assertRaises(self.manager.load_dump())

        self.manager.download_dump.side_effect = None
        self.manager.download_dump.return_value = os.path.join("tests", "fixtures", "dump.csv")

        # TODO : Build CSV test fixtures and make tests
