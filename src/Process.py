from datetime import datetime

import numpy as np
import matplotlib.pyplot as plt
from numpy import *
import soundfile as sf
import threading
import time
import os

class Process(threading.Thread):
    def __init__(self):
        self.nc=2
        self.nr=array.shape[0]
        self.array = []

    def run(self):
        my_array = self.array.reshape(self.nr * self.nc)
        ax = np.fft.fft(my_array)
        print(ax)
        x = ax[:len(ax) // 2][::-1]
        y = ax[(len(ax) // 2) + 1:][::-1]
        arr = np.concatenate((x, y))
        # plt.plot(arr)
        now = datetime.now()
        # to do ========== create file folder based on curent time/date lol
        dt_h = now.strftime("%d/%m/%Y-%H")
        dt_m = now.strftime("%d/%m/%Y-%H:%M")
        if not os.path.exists("F:\\" + "PythonProjects\RECORDINGAUDIO" + dt_h):
            os.mkdir("F:\\" + "PythonProjects\RECORDINGAUDIO" + dt_h)
            with open(dt_m + ".txt", 'a') as f:
                for item in arr:
                    f.write("%s " % item)
                f.write('\n')
        # plt.show()
