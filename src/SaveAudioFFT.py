import math
import os
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np

cwd=os.getcwd()
def saveAudioFFT(arr, slice):
    l = len(arr) // slice
    new_arr = []
    now = datetime.now()
    dt_d = now.strftime("%d-%m-%Y")
    dt_h = now.strftime("%d-%m-%Y-%H")
    dt_m = now.strftime("%d-%m-%Y-%H-%M")
    dt_s = now.strftime("%d-%m-%Y-%H-%M-%S")
    os.chdir(cwd)
    #with open("output.txt", 'a') as f:
       # f.write(dt_s + "\n")
    if not os.path.exists(cwd+ '\\' + dt_d):
        os.mkdir(dt_d)
        os.chdir(cwd+ "\\" + dt_d)
        if not os.path.exists(cwd+ "\\" + dt_d + "\\" + dt_h):
            os.mkdir(dt_h)
            os.chdir(cwd+ "\\" + dt_d + "\\" + dt_h)
            with open(dt_m + ".csv", 'a') as f:
                f.write("%s " % dt_s +", ")
                for i in range(l - 1):
                    if np.max(arr[i * slice:(i + 1) * slice]) == 0:
                        new_arr.append(1)
                    new_arr.append(10 * math.log10(np.absolute(np.max(arr[i * slice:(i + 1) * slice]))))
                    new_arr[i] = round(new_arr[i] * 100) / 100
                    f.write(str(new_arr[i])+" ")
                f.write('\n')
            print("Recording saved @ " + dt_m + " @ " + dt_s)
        else:
            os.chdir(cwd+ "\\" + dt_d + "\\" + dt_h)
            with open(dt_m + ".csv", 'a') as f:
                f.write("%s " % dt_s + ", ")
                for i in range(l - 1):
                    if np.max(arr[i * slice:(i + 1) * slice]) == 0:
                        new_arr.append(1)
                    new_arr.append(10 * math.log10(np.absolute(np.max(arr[i * slice:(i + 1) * slice]))))
                    new_arr[i] = round(new_arr[i] * 100) / 100
                    f.write(str(new_arr[i]) + " ")
                f.write('\n')
            print("Recording saved @ " + dt_m + " @ " + dt_s)
    else:
        os.chdir(cwd+ "\\" + dt_d)
        if os.path.exists(cwd+ "\\" + dt_d + "\\" + dt_h):
            os.chdir(cwd+ "\\" + dt_d + "\\" + dt_h)
            with open(dt_m + ".csv", 'a') as f:
                f.write("%s " % dt_s + ", ")
                for i in range(l - 1):
                    if np.max(arr[i * slice:(i + 1) * slice]) == 0:
                        new_arr.append(1)
                    new_arr.append(10 * math.log10(np.absolute(np.max(arr[i * slice:(i + 1) * slice]))))
                    new_arr[i] = round(new_arr[i] * 100) / 100
                    f.write(str(new_arr[i]) + " ")
                f.write('\n')
            print("Recording saved @ " + dt_m + " @ " + dt_s)
        else:
            os.mkdir(dt_h)
            os.chdir(cwd+ "\\" + dt_d + "\\" + dt_h)
            with open(dt_m + ".csv", 'a') as f:
                f.write("%s " % dt_s + ", ")
                for i in range(l - 1):
                    if np.max(arr[i * slice:(i + 1) * slice]) == 0:
                        new_arr.append(1)
                    new_arr.append(10 * math.log10(np.absolute(np.max(arr[i * slice:(i + 1) * slice]))))
                    new_arr[i] = round(new_arr[i] * 100) / 100
                    f.write(str(new_arr[i])+" ")
                f.write('\n')
            print("Recording saved @ " + dt_m + " @ " + dt_s)
