import threading
from queue import Queue
import sounddevice as sd

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
                available = 0
                self.myrecording = sd.rec(int(self.seconds * self.fs), samplerate=self.fs, channels=2)
                sd.wait()
                self.q.put(self.myrecording)
                # write('output.wav', fs, self.myrecording)
                available = 1
