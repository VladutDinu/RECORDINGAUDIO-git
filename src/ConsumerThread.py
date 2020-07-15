import threading
from ProducerThread import ProducerThread
import SaveAudioFFT
import numpy as np
class ConsumerThread(threading.Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs=None, verbose=None):
        super(ConsumerThread, self).__init__()
        self.target = target
        self.name = name
        self.myrecording = ProducerThread.myrecording
        return

    def reducsion(sefl, arr, slice):
        l = len(arr) // slice
        a = []
        for i in range(l):
            a.append(arr[i * slice:(i + 1) * slice])
        return a

    def agregare(self, a):
        arr = []
        new_arr=[]
        for i in range(len(a)):
            maxi, mini, avg, sum = np.max(a[i]), \
                                   np.min(a[i]), \
                                   np.average(a[i]), \
                                   np.sum(a[i])
            arr.append([maxi, mini, avg, sum], )
            new_arr.append(avg)
        return new_arr

    def run(self):
        red_array = []
        while True:
            _arr = ProducerThread.q.get()
            nrows = _arr.shape[0]
            ncols = 2
            my_array = _arr.reshape(nrows * ncols)
            ax = np.fft.fft(my_array)
            new_arr=self.agregare(self.reducsion(ax[:len(ax)//2], ProducerThread.fs//ProducerThread.CHUNK))
            # ax = scipy.fft.fft(my_array)
            # print(ax)
            # x = ax[:len(ax) // 2][::-1]
            # y = ax[(len(ax) // 2) + 1:][::-1]
            # arr = np.concatenate((x, y))
            arr=np.fft.fftshift(new_arr)
            #plt.plot(arr)
            SaveAudioFFT.saveAudioFFT(arr)
            #plt.show()

