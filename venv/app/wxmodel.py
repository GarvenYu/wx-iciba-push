#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import requests
import logging

logger = logging.getLogger(__name__)


class WxModel(object):
    app_id = "wx5d1e63fbeb5d285e"
    app_secret = "80529529c2dba23da1b9f013105748cd"
    template_id = "DcD875WtrNMm2YFmpeHtGnF99cLwL_iusxOsdBltq-c"
    access_token_url = "https://api.weixin.qq.com/cgi-bin/token?" \
                       "grant_type=client_credential&appid={app_id}&secret={app_secret}"
    get_user_list_url = "https://api.weixin.qq.com/cgi-bin/user/get?access_token={token}&next_openid="
    send_msg_url = "https://api.weixin.qq.com/cgi-bin/message/template/send?access_token={token}"

    def __init__(self):
        self.token = self.get_access_token()
        self.open_ids = self.get_user_list()

    def get_access_token(self):
        """获取调用接口的token"""
        resp = requests.get(self.access_token_url.format(app_id=self.app_id, app_secret=self.app_secret))
        if resp.status_code != 200:
            logger.error(resp.status_code)
        resp_str = json.loads(resp.text)
        if resp_str.get('errcode'):
            logger.error("Error!"+resp_str)
        return resp_str.get('access_token')

    def get_user_list(self):
        """
        获取用户列表
        @:return list ["OPENID1","OPENID2"]
        """
        resp = requests.get(self.get_user_list_url.format(token=self.token))
        if resp.status_code != 200:
            logger.error(resp.status_code)
        resp_str = json.loads(resp.text)
        if resp_str.get('errcode'):
            logger.error("Error!"+resp_str)
        return resp_str.get('data').get('openid')

    def send_message(self, msg_content):
        """调用接口发送模板消息"""
        for openid in self.open_ids:
            msg_body = {
                   "touser": openid,
                   "template_id": self.template_id,
                   "url": msg_content.get('fenxiang_img'),
                   "data": {
                            "content": {
                               "value": msg_content.get('content')
                            },
                            "note": {
                                "value": msg_content.get('note')
                            },
                            "love": {
                                "value": "{love}人喜欢".format(love=msg_content.get('love'))
                            },
                            "translation": {
                                "value": msg_content.get('translation')
                            }
                        }
            }
        requests.post(self.send_msg_url.format(token=self.token), data=json.dumps(msg_body))