#!/usr/bin/python
# _*_ coding: utf_8 _*_

import logging
import requests

logger = logging.getLogger()


class OFFApiConnector(object):
    """
    Wrapper around OFF API
    """

    BASE_URL = "https://world.openfoodfacts.org/%s"
    PRODUCT_URL = BASE_URL % "cgi/product_jqm2.pl"
    IMAGE_UPLOAD_URL = BASE_URL % "cgi/product_image_upload.pl"

    def __init__(self, username, password, user_agent=None):
        self.username = username
        self.password = password
        self.headers = {}
        if user_agent is not None:
            self.headers["User-Agent"] = user_agent

    def login(self):
        """
        Login user with given credentials. Return related session.
        """
        payload = {"user_id": self.username, "password": self.password}

        with requests.Session() as session:
            request = session.post(self.BASE_URL % "", data=payload, headers=self.headers)
            request_body = request.text
            if "You are connected as" not in request_body:
                raise ValueError("Incorrect Username or Password.")

            return session

    def get_product(self, barcode):
        url = "https://world.openfoodfacts.org/api/v0/product/%s.json" % barcode
        response = requests.get(url, headers=self.headers).json()
        if response.get("status") == 1:
            return response['product']

    def post_product(self, off_food, comment=None, safe_insert=False):
        """
        Add or edit remote OFF product with your local version

        :safe_insert:       bool        Create only - if product already exists, skip update
        :comment:           str         Add comment to your update
        """
        if safe_insert and self.get_product(off_food.code) is not None:
            logger.info("Product #%s already already exists and safe_insert mode activated, skipping..." % off_food.code)
            return

        payload = {"user_id": self.username, "password": self.password, "comment": comment}
        payload.update(off_food.serialize_for_off_api())

        requests.post(self.PRODUCT_URL, data=payload, headers=self.headers)

    def upload_image(self, code, img_file, img_field="other"):
        """
        Upload an image to openfoodfacts

        img_field in ['front', 'ingredients', 'nutrition', 'other']
        """
        requests.post(
            self.IMAGE_UPLOAD_URL,
            data={
                "user_id": self.username,
                "password": self.password,
                "code": code,
                "imagefield": img_field
            },
            files={"imgupload_%s" % img_field: img_file},
            headers=self.headers
        )
