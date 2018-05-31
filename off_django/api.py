#!/usr/bin/python
# _*_ coding: utf_8 _*_

import requests


class OFFApiConnector(object):
    """
    Wrapper around OFF API
    """

    BASE_URL = "https://world.openfoodfacts.org/%s"

    def __init__(self, username, password):

        self.username = username
        self.password = password

        self.PRODUCT_URL = self.BASE_URL % "cgi/product_jqm2.pl"

    def login(self):
        """
        Login user with given credentials. Return related session.
        """
        payload = {"user_id": self.username, "password": self.password}

        with requests.Session() as session:
            request = session.post(self.BASE_URL % "", data=payload)
            request_body = request.text
            if "You are connected as" not in request_body:
                raise ValueError("Incorrect Username or Password.")

            return session

    def post_product(self, off_food):
        """
        Add or edit remote OFF product with your local version
        """
        payload = {"user_id": self.username, "password": self.password}
        payload.update(off_food.serialize_for_off_api())

        requests.post(self.PRODUCT_URL, data=payload)
