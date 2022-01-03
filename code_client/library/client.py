# -*- coding: utf-8 -*-
import socket


class client(object):
    def __init__(self, file, method):
        self.address = ('101.42.97.164', 8080)  # 服务器ip:101.42.97.164
        self.file_path = file
        self.method = method

    def send(self):
        print('sending {}'.format(self.file_path))
        data = self.file_deal()
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(self.address)
        sock.send('{}|{}|{}'.format(self.method, len(data), "test").encode())
        reply = sock.recv(1024)
        if 'ok' == reply.decode():
            go = 0
            total = len(data)
            while go < total:
                data_to_send = data[go:go + 1024]
                sock.send(data_to_send)
                go += len(data_to_send)
            reply = sock.recv(1024)
            method_back, data = reply.decode().split("|")
            if method_back == "judge_audio":
                sock.close()
                return data
            if method_back == "img":
                sock.close()
                return data

    def file_deal(self):
        file = open(self.file_path, 'rb')
        mes = file.read()
        file.close()
        return mes

    def set_file(self, path):
        self.file_path = path


if __name__ == "__main__":
    pass
