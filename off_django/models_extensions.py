#!/usr/bin/python
# _*_ coding: utf_8 _*_

import ast

from django.db import models


class ListField(models.TextField):
    description = "Stores a python list"

    def __init__(self, *args, **kwargs):
        super(ListField, self).__init__(*args, **kwargs)

    def to_python(self, value):
        if not value:
            value = []

        if isinstance(value, list):
            return value

        return ast.literal_eval(value)

    def from_db_value(self, value, expression, connection, *args, **kwargs):
        return self.to_python(value)

    def get_prep_value(self, value):
        if value is None:
            return value

        return str(value)

    def value_to_string(self, obj):
        value = self.value_from_object(obj)
        return self.get_db_prep_value(value, None)
