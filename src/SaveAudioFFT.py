import os
from datetime import datetime

cwd=os.getcwd()
def saveAudioFFT(arr):
    now = datetime.now()
    dt_d = now.strftime("%d-%m-%Y")
    dt_h = now.strftime("%d-%m-%Y-%H")
    dt_m = now.strftime("%d-%m-%Y-%H-%M")
    dt_s = now.strftime("%d-%m-%Y-%H-%M-%S")
    os.chdir(cwd)
    with open("output.txt", 'a') as f:
        f.write(dt_s + "\n")
    if not os.path.exists(cwd+ '\\' + dt_d):
        os.mkdir(dt_d)
        os.chdir(cwd+ "\\" + dt_d)
        if not os.path.exists(cwd+ "\\" + dt_d + "\\" + dt_h):
            os.mkdir(dt_h)
            os.chdir(cwd+ "\\" + dt_d + "\\" + dt_h)
            with open(dt_m + ".txt", 'a') as f:
                for item in arr:
                    f.write("%s " % item)
                f.write('\n')
            print("Recording saved @ " + dt_m + " @ " + dt_s)
        else:
            os.chdir(cwd+ "\\" + dt_d + "\\" + dt_h)
            with open(dt_m + ".txt", 'a') as f:
                for item in arr:
                    f.write("%s " % item)
                f.write('\n')
            print("Recording saved @ " + dt_m + " @ " + dt_s)
    else:
        os.chdir(cwd+ "\\" + dt_d)
        if os.path.exists(cwd+ "\\" + dt_d + "\\" + dt_h):
            os.chdir(cwd+ "\\" + dt_d + "\\" + dt_h)
            with open(dt_m + ".txt", 'a') as f:
                for item in arr:
                    f.write("%s " % item)
                f.write('\n')
            print("Recording saved @ " + dt_m + " @ " + dt_s)
        else:
            os.mkdir(dt_h)
            os.chdir(cwd+ "\\" + dt_d + "\\" + dt_h)
            with open(dt_m + ".txt", 'a') as f:
                for item in arr:
                    f.write("%s " % item)
                f.write('\n')
            print("Recording saved @ " + dt_m + " @ " + dt_s)