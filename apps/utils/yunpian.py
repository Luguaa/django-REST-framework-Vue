__author__ = 'Luguaa'
__date__ = '2020/5/3 18:32'

import requests
import json


class YunPian(object):

    def __init__(self, api_key):
        self.api_key = api_key
        self.single_send_url = "https://sms.yunpian.com/v2/sms/single_send.json"

    def send_sms(self, code, mobile):
        params = {
            'apikey': self.api_key,
            'mobile': mobile,
            'text': "【张鑫楠test】您的验证码是{code}。如非本人操作，请忽略本短信".format(code=code),
        }

        response = requests.post(self.single_send_url, data=params)
        re_dict = json.loads(response.text)
        return re_dict


if __name__ == '__main__':
    yun_pian = YunPian("0f8b8ce213e2dff78a3aaadc6b1489b1")
    yun_pian.send_sms("2020", "15252470494")
