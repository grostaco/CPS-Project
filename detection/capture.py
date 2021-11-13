import cv2.cv2 as cv2
from queue import Queue
import numpy as np


class VideoCapture:
    def __init__(self, device_index: int):
        self.capture = cv2.VideoCapture(device_index)
        self.buffer_rq: Queue[np.ndarray] = Queue()

    def read(self):
        if self.buffer_rq.empty():
            return self.capture.read()
        return self.buffer_rq.get_nowait()

    def feed(self, frame: np.ndarray):
        self.buffer_rq.queue(frame)
