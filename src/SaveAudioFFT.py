import math
import os
from datetime import datetime
import numpy as np
cwd = os.getcwd()
def saveAudioFFT(arr, slice):
    now = datetime.now()
    dt_d = now.strftime("%d-%m-%Y")
    dt_h = now.strftime("%d-%m-%Y-%H")
    dt_m = now.strftime("%d-%m-%Y-%H-%M")
    dt_s = now.strftime("%d-%m-%Y-%H-%M-%S")
    os.chdir(cwd)
    # with open("output.txt", 'a') as f:
    # f.write(dt_s + "\n")
    # Code to establish the file path
    if not os.path.exists(cwd + '\\' + dt_d):
        os.mkdir(dt_d)
        os.chdir(cwd + "\\" + dt_d)
        if not os.path.exists(cwd + "\\" + dt_d + "\\" + dt_h):
            os.mkdir(dt_h)
            os.chdir(cwd + "\\" + dt_d + "\\" + dt_h)
        else:
            os.chdir(cwd + "\\" + dt_d + "\\" + dt_h)
    else:
        os.chdir(cwd + "\\" + dt_d)
        if os.path.exists(cwd + "\\" + dt_d + "\\" + dt_h):
            os.chdir(cwd + "\\" + dt_d + "\\" + dt_h)
        else:
            os.mkdir(dt_h)
            os.chdir(cwd + "\\" + dt_d + "\\" + dt_h)
    # Code to write the array into file
    # string_array = create_string_from_array_to_write_in_file(arr, dt_s, ',', slice)
    # with open(dt_m + ".txt", "a") as f:
    #     f.write(string_array)
    #     f.flush()
    write_array_to_file(arr, dt_s, dt_m, ',', slice)
    print("Recording saved @ " + dt_m + " @ " + dt_s)
def create_string_from_array_to_write_in_file(array, date_second, delimiter, slice):
    l = len(array) // slice
    string = "%s " % date_second + delimiter
    new_arr = []
    for i in range(l):
        if np.max(array[i * slice:(i + 1) * slice]) == 0:
            new_arr.append(1)
        new_arr.append(10 * math.log10(np.absolute(np.max(array[i * slice:(i + 1) * slice]))))
        new_arr[i] = round(new_arr[i] * 100) / 100
        string += str(new_arr[i]) + delimiter
    return string + '\n'
def write_array_to_file(array, date_second, date_minute, delimiter, slice):
    l = len(array) // slice
    new_arr = []
    with open(date_minute + ".txt", "a") as f:
        f.write("%s " % date_second + delimiter)
        for i in range(l - 1):
            if np.max(array[i * slice:(i + 1) * slice]) == 0:
                new_arr.append(1)
            new_arr.append(10 * math.log10(np.absolute(np.max(array[i * slice:(i + 1) * slice]))))
            new_arr[i] = round(new_arr[i] * 100) / 100
            f.write(str(new_arr[i]) + delimiter)
        f.write('\n')
        f.flush()