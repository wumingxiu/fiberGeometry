
import pdb
import numpy as np
import time
import cv2
from method.toolkit import timing
try:
    import SDK.MindPy.MindPyCEx.MindPy as mdp
except WindowsError:
    import MindPy.MindPyCEx.MindPy as mdp


class GetRawImg(object):
    """docstring for getRawImg"""
    def __init__(self, ):
        super(GetRawImg, self).__init__()
        self.limit = 2592*1944
        print dir(mdp)

        self.hand = mdp.initCamera()

    # @timing
    def get(self):
        """ get 0.0990002155304 s
            get raw dll 0.0910000801086 s
            create np.array 0.00600004196167 s
            reshape 0s
        """
        try:
            # md = mdp.getRawImg(self.limit)
            md = mdp.getRawImg()
            # ValueError: get raw image error: -12

        except Exception, e:
            raise e

        npArray = md.reshape(1944, 2592)
        return npArray

    def unInitCamera(self):
        mdp.uninitCamera()




