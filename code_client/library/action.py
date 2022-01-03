# -*- coding: utf-8 -*-
import time
import busio
from board import SCL, SDA
from adafruit_motor import servo
from adafruit_pca9685 import PCA9685


class action(object):
    def __init__(self):
        self.i2c = busio.I2C(SCL, SDA)
        self.pca = PCA9685(self.i2c)
        self.pca.frequency = 50

        # 舵机与端口绑定
        # 右眼球上下
        self.servo0 = servo.Servo(self.pca.channels[0], min_pulse=500, max_pulse=2500)
        # 右眼球左右
        self.servo1 = servo.Servo(self.pca.channels[1], min_pulse=500, max_pulse=2500)
        # 左眼皮
        self.servo2 = servo.Servo(self.pca.channels[2], min_pulse=500, max_pulse=2500)
        # 左眼球上下
        self.servo3 = servo.Servo(self.pca.channels[3], min_pulse=500, max_pulse=2500)
        # 右眉毛
        self.servo4 = servo.Servo(self.pca.channels[4], min_pulse=500, max_pulse=2500)
        # 右眼皮
        self.servo5 = servo.Servo(self.pca.channels[5], min_pulse=500, max_pulse=2500)
        # 左眼球左右
        self.servo6 = servo.Servo(self.pca.channels[6], min_pulse=500, max_pulse=2500)
        # 左眉毛
        self.servo7 = servo.Servo(self.pca.channels[7], min_pulse=500, max_pulse=2500)
        # 嘴巴
        self.servo8 = servo.Servo(self.pca.channels[8], min_pulse=500, max_pulse=2500)
        # 头部左右
        self.servo9 = servo.Servo(self.pca.channels[9], min_pulse=500, max_pulse=2500)
        # 头部上下
        self.servo10 = servo.Servo(self.pca.channels[12], min_pulse=500, max_pulse=2500)

    def initial(self):
        self.servo0.angle = 108
        self.servo1.angle = 90
        self.servo2.angle = 72
        self.servo3.angle = 72
        self.servo4.angle = 72
        self.servo5.angle = 72
        self.servo6.angle = 90
        self.servo7.angle = 108
        self.servo8.angle = 110
        self.servo9.angle = 90
        self.servo10.angle = 76

    def sad(self, event):
        while event.isSet():
            time.sleep(0.3)
            self.servo0.angle = 108
            self.servo1.angle = 90
            self.servo2.angle = 72
            self.servo3.angle = 72
            self.servo4.angle = 72
            self.servo5.angle = 72
            self.servo6.angle = 90
            self.servo7.angle = 108
            self.servo8.angle = 85
            self.servo9.angle = 90
            self.servo10.angle = 76

            time.sleep(0.3)
            self.servo0.angle = 108
            self.servo1.angle = 90
            self.servo2.angle = 72
            self.servo3.angle = 72
            self.servo4.angle = 72
            self.servo5.angle = 72
            self.servo6.angle = 90
            self.servo7.angle = 108
            self.servo8.angle = 110
            self.servo9.angle = 90
            self.servo10.angle = 76

        time.sleep(0.3)
        self.initial()

    def happy(self, event):
        time.sleep(0.3)
        self.servo0.angle = 90
        self.servo1.angle = 90
        self.servo2.angle = 72
        self.servo3.angle = 90
        self.servo4.angle = 90
        self.servo5.angle = 72
        self.servo6.angle = 90
        self.servo7.angle = 90
        self.servo8.angle = 85
        self.servo9.angle = 90
        self.servo10.angle = 76

        time.sleep(0.3)
        self.servo0.angle = 90
        self.servo1.angle = 90
        self.servo2.angle = 72
        self.servo3.angle = 90
        self.servo4.angle = 72
        self.servo5.angle = 72
        self.servo6.angle = 90
        self.servo7.angle = 108
        self.servo8.angle = 110
        self.servo9.angle = 90
        self.servo10.angle = 76

        time.sleep(0.3)
        self.servo0.angle = 90
        self.servo1.angle = 90
        self.servo2.angle = 72
        self.servo3.angle = 90
        self.servo4.angle = 108
        self.servo5.angle = 72
        self.servo6.angle = 90
        self.servo7.angle = 72
        self.servo8.angle = 85
        self.servo9.angle = 90
        self.servo10.angle = 76

        time.sleep(0.3)
        self.servo0.angle = 90
        self.servo1.angle = 90
        self.servo2.angle = 72
        self.servo3.angle = 90
        self.servo4.angle = 72
        self.servo5.angle = 72
        self.servo6.angle = 90
        self.servo7.angle = 108
        self.servo8.angle = 110
        self.servo9.angle = 90
        self.servo10.angle = 76

        time.sleep(0.3)
        self.servo0.angle = 90
        self.servo1.angle = 90
        self.servo2.angle = 72
        self.servo3.angle = 90
        self.servo4.angle = 72
        self.servo5.angle = 72
        self.servo6.angle = 90
        self.servo7.angle = 108
        self.servo8.angle = 85
        self.servo9.angle = 90
        self.servo10.angle = 76

        time.sleep(0.3)
        self.servo0.angle = 90
        self.servo1.angle = 90
        self.servo2.angle = 72
        self.servo3.angle = 90
        self.servo4.angle = 90
        self.servo5.angle = 72
        self.servo6.angle = 90
        self.servo7.angle = 90
        self.servo8.angle = 110
        self.servo9.angle = 90
        self.servo10.angle = 76

        time.sleep(0.3)
        self.servo0.angle = 90
        self.servo1.angle = 90
        self.servo2.angle = 117
        self.servo3.angle = 90
        self.servo4.angle = 90
        self.servo5.angle = 117
        self.servo6.angle = 90
        self.servo7.angle = 90
        self.servo8.angle = 85
        self.servo9.angle = 90
        self.servo10.angle = 76

        time.sleep(0.3)
        self.servo0.angle = 90
        self.servo1.angle = 90
        self.servo2.angle = 72
        self.servo3.angle = 90
        self.servo4.angle = 90
        self.servo5.angle = 72
        self.servo6.angle = 90
        self.servo7.angle = 90
        self.servo8.angle = 110
        self.servo9.angle = 90
        self.servo10.angle = 76

        time.sleep(0.3)
        self.servo0.angle = 90
        self.servo1.angle = 90
        self.servo2.angle = 117
        self.servo3.angle = 90
        self.servo4.angle = 90
        self.servo5.angle = 117
        self.servo6.angle = 90
        self.servo7.angle = 90
        self.servo8.angle = 85
        self.servo9.angle = 90
        self.servo10.angle = 72

        time.sleep(0.3)
        self.servo0.angle = 90
        self.servo1.angle = 90
        self.servo2.angle = 72
        self.servo3.angle = 90
        self.servo4.angle = 90
        self.servo5.angle = 72
        self.servo6.angle = 90
        self.servo7.angle = 90
        self.servo8.angle = 110
        self.servo9.angle = 90
        self.servo10.angle = 76

        while event.isSet():
            time.sleep(0.3)
            self.servo0.angle = 90
            self.servo1.angle = 90
            self.servo2.angle = 72
            self.servo3.angle = 90
            self.servo4.angle = 90
            self.servo5.angle = 72
            self.servo6.angle = 90
            self.servo7.angle = 90
            self.servo8.angle = 85
            self.servo9.angle = 76
            self.servo10.angle = 76

            time.sleep(0.3)
            self.servo0.angle = 90
            self.servo1.angle = 90
            self.servo2.angle = 72
            self.servo3.angle = 90
            self.servo4.angle = 90
            self.servo5.angle = 72
            self.servo6.angle = 90
            self.servo7.angle = 90
            self.servo8.angle = 110
            self.servo9.angle = 121
            self.servo10.angle = 76

        time.sleep(0.3)
        self.initial()

    def clam(self, event):
        while event.isSet():
            time.sleep(0.3)
            self.servo0.angle = 90
            self.servo1.angle = 90
            self.servo2.angle = 90
            self.servo3.angle = 90
            self.servo4.angle = 90
            self.servo5.angle = 90
            self.servo6.angle = 90
            self.servo7.angle = 90
            self.servo8.angle = 85
            self.servo9.angle = 90
            self.servo10.angle = 76

            time.sleep(0.3)
            self.servo0.angle = 90
            self.servo1.angle = 90
            self.servo2.angle = 90
            self.servo3.angle = 90
            self.servo4.angle = 90
            self.servo5.angle = 90
            self.servo6.angle = 90
            self.servo7.angle = 90
            self.servo8.angle = 110
            self.servo9.angle = 90
            self.servo10.angle = 76

        time.sleep(0.3)
        self.initial()


if __name__ == "__main__":
    pass
