import numpy as np
import matplotlib.pyplot as plt
from numpy import *
import soundfile as sf
import threading
import time
import os
import sounddevice as sd

class AudioRecorder(threading.Thread):
    def __init__(self, fsample, seconds, available):
        self.fs=fsample
        self.sec=seconds
        self.av=available
        self.myrecording=[]


    def run(self, fsample, seconds):
        myrecording = sd.rec(int(seconds * self.fs), samplerate=self.fs, channels=2)
        sd.wait()
        available = 1
        return myrecording
