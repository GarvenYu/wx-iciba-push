#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json
from .wxmodel import WxModel


class iciba(object):
    iciba_api_url = "http://open.iciba.com/dsapi/"

    def __init__(self):
        self.wx_model = WxModel()
        # 获取信息
        self.msg_content = self.get_iciba_words()

    def get_iciba_words(self, date=None, file=None, type=None):
        response = requests.get(self.iciba_api_url)
        if response.status_code == 200:
            return json.loads(response.text, encoding="UTF-8")

    def run(self):
        # 发送消息到手机端
        self.wx_model.send_message(self.msg_content)
