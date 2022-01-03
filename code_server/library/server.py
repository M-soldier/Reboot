# -*- coding: utf-8 -*-
import socket
import cv2
from library import voiceRecognize
from library import faceRecognize


class server(object):
    def __init__(self):
        self.LOCAL_IP = '0.0.0.0'
        self.PORT = 8080
        self.voice = voiceRecognize.voiceRecognize()
        self.face = faceRecognize.faceRecognize()
        self.count_img = 1
        self.count_audio = 1

    def on_server(self):
        print("***on_server***")
        self.voice.load_audio_db("../record/voiceRecognize/audio_db".encode("ascii"))
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind((self.LOCAL_IP, self.PORT))
        sock.listen(3)
        while True:
            sc, sc_name = sock.accept()
            print('收到{}请求'.format(sc_name))
            info = sc.recv(1024)
            method, length, file_name = info.decode().split('|')
            new_file = ""
            if method == "img":
                print("image:{}".format(self.count_img))
                new_file = '../data/image/' + str(self.count_img).zfill(4) + '.jpg'
                self.count_img += 1
            if method == "judge_audio":
                new_file = '../data/audio/' + str(self.count_audio).zfill(4) + '.wav'
                self.count_audio += 1
            if length and file_name:
                sc.send(b'ok')
                file = b''
                total = int(length)
                get = 0
                while get < total:
                    data = sc.recv(1024)
                    file += data
                    get = get + len(data)
                if file:
                    print("文件已接收！！！")
                    with open(new_file, "wb") as f:
                        f.write(file[:])
                    if method == "judge_audio":
                        name, p = self.voice.recognition(new_file)
                        print("p : {}\n".format(p))
                        if p > 0.71:
                            sc.send("{}|{}".format("judge_audio", "True").encode())
                        else:
                            sc.send("{}|{}".format("judge_audio", "False").encode())

                    if method == "img":
                        frame = cv2.imread(new_file, 1)
                        back = self.face.evaluate(frame)
                        sc.send("{}|{}".format("img", back).encode())
            sc.close()


if __name__ == '__main__':
    pass
