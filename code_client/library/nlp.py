# -*- coding: utf-8 -*-
import requests
import time
import hashlib
import base64


class nlp(object):
    def __init__(self):
        self.URL = "http://openapi.xfyun.cn/v2/aiui"
        self.RESULT_LEVEL = "complete"
        self.AUTH_ID = "2894c985bf8b1111c6728db79d3479ae"
        self.DATA_TYPE = "audio"
        self.SAMPLE_RATE = "16000"
        self.SCENE = "main"
        self.APPID = "5beaacac"
        self.API_KEY = "4227d60d150c455db467b623d7ae183d"
        self.FILE_PATH = "./data/record.wav"

    def build_header(self):
        curTime = str(int(time.time()))
        param = "{\"result_level\":\"" + self.RESULT_LEVEL + "\",\"auth_id\":\"" + self.AUTH_ID + "\",\"data_type\":\"" + self.DATA_TYPE + "\",\"sample_rate\":\"" + self.SAMPLE_RATE + "\",\"scene\":\"" + self.SCENE + "\"}"
        paramBase64 = base64.b64encode(param.encode('utf-8'))
        m2 = hashlib.md5()
        m2.update((self.API_KEY + curTime + str(paramBase64, 'utf-8')).encode('utf-8'))
        checkSum = m2.hexdigest()

        header = {
            'X-CurTime': curTime,
            'X-Param': paramBase64,
            'X-Appid': self.APPID,
            'X-CheckSum': checkSum,
        }
        return header

    def read_file(self):
        file = open(self.FILE_PATH, 'rb')
        Data = file.read()
        return Data

    def get_text(self):
        r = requests.post(self.URL, headers=self.build_header(), data=self.read_file())
        dic_json = r.json()
        for i in dic_json['data']:
            if i['sub'] == "nlp" and i['intent'] != {}:
                try:
                    text = i['intent']['answer']['text']
                except:
                    text = "我没有听明白你在说什么！"
                with open("./data/data.txt", 'a') as file_object:
                    file_object.write('我 :' + i['intent']['text'] + '\n')
                    file_object.write('机器人 :' + text + '\n\n')
                    text_people = i['intent']['text']
                break
        else:
            text = None
            text_people = None
            print('没有检测到人声')

        return text, text_people


if __name__ == "__main__":
    pass
