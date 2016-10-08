from threading import Thread
from PyQt4.QtCore import QObject, pyqtSignal
from SDK.mindpy import GetRawImg
import cv2
import numpy as np
from method.edgedetect import ErodeDilate
from method.contour import findContours
from method.contour import FitEllipse

from pattern.edge import ExtractEdge
from pattern.classify import G652Classify

from method.toolkit import Cv2ImShow, Cv2ImSave
import time
import pdb
import collections


class Model(Thread,QObject):
    """docstring for Model"""
    returnImg = pyqtSignal(object)
    # returnFiberResult = pyqtSignal(object)

    def __init__(self, ):
        Thread.__init__(self)
        QObject.__init__(self)
        super(Model, self).__init__()
        self.setDaemon(True)
        self.show = Cv2ImShow()
        self.save = Cv2ImSave()
        self.getRawImg = GetRawImg()
        self.imgQueue = collections.deque(maxlen = 5)
        self.fiberResult = {}


    def run(self):
        while True:
            img = self._getImg()
            self.returnImg.emit(img)

    def _getImg(self):
        img = self.getRawImg.get()
        self.imgQueue.append(img)
        return img[::4,::4]


    def mainCalculate(self):
        Thread(target = self._calcImg2).start()


    def _calcImg(self):
        imgs = list(self.imgQueue)
        isImgAdded = True
        for img in imgs:
            img = ErodeDilate().run(img)
            if isImgAdded:
                imgadd = img
                isImgAdded = False
            else:
                imgadd = imgadd + img
        img = imgadd/3
        img = cv2.medianBlur(img, 9)
        img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 17, 7)
        self.show.show('edge', img[::4,::4])
        FitEllipse().ellipseForIfCondition(img)

    def _calcImg2(self):
        imgs = list(self.imgQueue)
        imgAllor = np.zeros(imgs[0].shape, dtype=imgs[0].dtype)
        for img in imgs:
            img = ExtractEdge().run(img)
            # self.show.show('img', img[::4,::4])
            imgAllor = cv2.bitwise_or(imgAllor, img)
        img = cv2.medianBlur(imgAllor, 5)
        # img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 17, 7)
        self.show.show('edge', img[::4,::4])
        classify = G652Classify()
        classify.find(img)
        classify.getResult()

        # coreResult = self.fiberResult.get('core', (0))
        # cladResult = self.fiberResult.get('clad', (0))
        #
        # coreCore, coreRadius, angle = coreResult
        # cladCore, cladRadius, angle = cladResult
        # # concentricity =


