# -*- coding: utf-8 -*-
import os
import shutil

import numpy as np
import torch

from library.reader import load_audio


class Init(object):
    def __init__(self):
        self.device = torch.device("cuda")
        self.model = torch.jit.load("../record/voiceRecognize/models/resnet34.pth")
        self.model.to(self.device)
        self.model.eval()

    def infer(self, audio_path):
        input_shape = eval('(1, 257, 257)')
        data = load_audio(audio_path, mode='infer', spec_len=input_shape[2])
        data = data[np.newaxis, :]
        data = torch.tensor(data, dtype=torch.float32, device=self.device)
        # 执行预测
        feature = self.model(data)
        return feature.data.cpu().numpy()


class voiceRecognize(object):
    def __init__(self):
        self.person_feature = []
        self.person_name = []
        self.INIT = Init()

    # 加载要识别的音频库
    def load_audio_db(self, audio_db_path):
        audios = os.listdir(audio_db_path)
        for audio in audios:
            path = os.path.join(audio_db_path, audio)
            name = audio[:-4]
            feature = self.INIT.infer(path)[0]
            self.person_name.append(name)
            self.person_feature.append(feature)
            # print("Loaded %s audio." % name)

    def recognition(self, path):
        name = ''
        pro = 0
        feature = self.INIT.infer(path)[0]
        for i, person_f in enumerate(self.person_feature):
            dist = np.dot(feature, person_f) / (np.linalg.norm(feature) * np.linalg.norm(person_f))
            if dist > pro:
                pro = dist
                name = self.person_name[i]
        return name, pro

    # 声纹注册
    def register(self, path, user_name):
        save_path = os.path.join("../record/voiceRecognize/audio_db", user_name + os.path.basename(path)[-4:])
        shutil.move(path, save_path)
        feature = self.INIT.infer(save_path)[0]
        self.person_name.append(user_name)
        self.person_feature.append(feature)


if __name__ == '__main__':
    pass
