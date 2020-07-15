import math
import threading
from queue import Queue

import numpy as np
import sounddevice as sd

import SaveAudioFFT


class ProducerThread(threading.Thread):
    myrecording = []
    fs = 44100
    seconds = 1
    CHUNK = 2205
    q = Queue(10)
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs=None, verbose=None):
        super(ProducerThread, self).__init__()
        self.target = target
        self.name = name
        self.myrecording = []

    def run(self):
        while True:
            if not self.q.full():
                self.myrecording = sd.rec(int(self.seconds * self.fs), samplerate=self.fs, channels=2)
                sd.wait()
                _arr = self.myrecording
                nrows = _arr.shape[0]
                ncols = 2
                my_array = _arr.reshape(nrows * ncols)
                ax = np.fft.fft(my_array)
                SaveAudioFFT.saveAudioFFT(ax[:len(ax) // 2],ProducerThread.fs // ProducerThread.CHUNK)

