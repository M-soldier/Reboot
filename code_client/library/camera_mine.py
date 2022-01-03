import cv2
import numpy as np
from jetcam.csi_camera import CSICamera
from library import client


class camera(object):
    def __init__(self):
        self.num = 1
        self.count = 1
        self.CLIENT = client.client("", "img")
        self.FERarray = np.zeros(7)
        self.camera = CSICamera(capture_device=0, width=640, height=480)

    def start(self):
        while True:
            image = self.camera.read()
            cv2.imwrite('./data/image/' + str(self.num).zfill(4) + '.jpg', image)
            self.CLIENT.file_path = "./data/image/" + str(self.num).zfill(4) + '.jpg'
            self.FERarray[int(self.CLIENT.send())] += 1
            self.num += 1
            cv2.waitKey(1)
            if self.num - self.count == 5:
                break
        self.count += 5
        return np.argmax(self.FERarray)


if __name__ == "__main__":
    pass
