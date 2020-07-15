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

    def reducsion(sefl, arr, slice):
        l = len(arr) // slice
        a = []
        _arr = []
        new_arr = []
        for i in range(l-1):
            if np.max(arr[i * slice:(i + 1) * slice]) == 0:
                new_arr.append(1)
            new_arr.append(10 * math.log10(np.absolute( np.max(arr[i * slice:(i + 1) * slice]))))
            new_arr[i]=round(new_arr[i]*100)/100
        return new_arr

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
                #new_arr = self.reducsion(, )
                #arr = np.fft.fftshift(new_arr)
                SaveAudioFFT.saveAudioFFT(ax[:len(ax) // 2],ProducerThread.fs // ProducerThread.CHUNK)

