#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json
from app.wxmodel import WxModel


class iciba(object):
    iciba_api_url = "http://open.iciba.com/dsapi/"

    def __init__(self):
        self.wx_model = WxModel()

    def get_iciba_words(self, date=None, file=None, type=None):
        response = requests.get(self.iciba_api_url)
        if response.status_code == 200:
            return json.loads(response.text, encoding="UTF-8")

    def run(self):
        msg_content = self.get_iciba_words()
        self.wx_model.send_message(msg_content)


if __name__ == "__main__":
    iciba_instance = iciba()
    iciba_instance.run()
