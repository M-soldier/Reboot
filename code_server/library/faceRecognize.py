# -*- coding: utf-8 -*-
import torch
from torch.autograd import Variable
import numpy as np
from PIL import Image
from library import transforms
from skimage.transform import resize
from library.vgg import VGG
import os

os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'

class faceRecognize(object):
    def __init__(self):
        self.class_names = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']
        self.c = 0
        self.cut_size = 44
        self.transform_test = transforms.Compose([
            transforms.TenCrop(self.cut_size),
            transforms.Lambda(lambda crops: torch.stack([transforms.ToTensor()(crop) for crop in crops])),
        ])
        self.checkpoint = torch.load('../record/faceRecognize/models/PrivateTest_model.t7', map_location='cpu')

    def rgb2gray(self, rgb):
        return np.dot(rgb[..., :3], [0.299, 0.587, 0.114])

    def evaluate(self, frame):
        gray = self.rgb2gray(frame)

        gray = resize(gray, (48, 48), mode='symmetric').astype(np.uint8)  # 这一步用时10秒左右

        img = gray[:, :, np.newaxis]  # 修改成48*48*1

        img = np.concatenate((img, img, img), axis=2)  # (48, 48, 3)
        img = Image.fromarray(img)  # 实现array到image的转换
        inputs = self.transform_test(img)  # 查看当前Tensor的维度。torch.Size([10, 3, 44, 44])

        net = VGG('VGG19')
        net.load_state_dict(self.checkpoint['net'])
        net.eval()

        ncrops, c, h, w = np.shape(inputs)

        inputs = inputs.view(-1, c, h, w)
        with torch.no_grad():
            inputs = Variable(inputs)

        outputs = net(inputs)  # 这一步在jetson nano上费时11秒左右

        outputs_avg = outputs.view(ncrops, -1).mean(0)  # avg over crops

        _, predicted = torch.max(outputs_avg.data, 0)

        if int(predicted.cpu().numpy()) == 0:
            print('愤怒')
            return "0"
        elif int(predicted.cpu().numpy()) == 1:
            print('恶心')
            return "1"
        elif int(predicted.cpu().numpy()) == 2:
            print('恐惧')
            return "2"
        elif int(predicted.cpu().numpy()) == 3:
            print('高兴')
            return "3"
        elif int(predicted.cpu().numpy()) == 4:
            print('悲伤')
            return "4"
        elif int(predicted.cpu().numpy()) == 5:
            print('震惊')
            return "5"
        else:
            print('中立')
            return "6"


if __name__ == "__main__":
    pass
