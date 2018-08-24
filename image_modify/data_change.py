import cv2
import os
import re

path = 'save_data/'

for a, b, dirs in os.walk(path):
    for filename in dirs:
        if filename[-1] == 'g':
            continue
        with open(path + filename) as f:
            with open('data_left/' + filename[0:-4] + '_l.txt', 'w') as fl:
                with open('data_right/' + filename[0:-4] + '_r.txt', 'w') as fr:
                    ct = 0
                    npoints = 0
                    hpoints = 0
                    flag = 0
                    cut_y = 0
                    for line in f.readlines():
                        if line[0] == 'n':
                            npoints = int(line[9:11])
                            if npoints > 20:
                                hpoints = int((npoints - 1) / 2)
                                fl.write("points: %d\n" % hpoints)
                                fr.write("points: %d\n" % hpoints)
                                print(npoints, hpoints)
                            else:
                                flag = 1

                            ct += 1
                            continue

                        if ct == 1:
                            l1 = line.split(" ", 1)
                            cut_y = int(float(l1[0]))
                            img0 = cv2.imread(path + filename[0:-4] + '.jpg', 3)
                            x0 = img0.shape[0]
                            y0 = img0.shape[1]
                            cropped1 = img0[0:x0, 0:cut_y]
                            cropped2 = img0[0:x0, cut_y:y0]
                            cv2.imwrite('data_left/' + filename[0:-4] + '_l.jpg', cropped1)
                            cv2.imwrite('data_right/' + filename[0:-4] + '_r.jpg', cropped2)
                            ct += 1
                            continue

                        if ct == 2:
                            l2 = line.split(" ", 1)
                            tst = int(float(l2[0]))
                            if flag == 1:
                                if tst > cut_y:
                                    fl.write("points: %d\n" % 0)
                                    fr.write("points: %d\n" % (npoints - 1))
                                    flag = 2
                                else:
                                    fr.write("points: %d\n" % 0)
                                    fl.write("points: %d\n" % (npoints - 1))

                        if flag == 0:
                            if ct <= hpoints + 1:
                                fl.write(line)
                            else:
                                ln = line.split(" ", 1)
                                yy = float(ln[0])
                                yy -= cut_y
                                fr.write(str(yy) + " " + ln[1])
                        elif flag == 1:
                            fl.write(line)
                        else:
                            ln = line.split(" ", 1)
                            yy = float(ln[0])
                            yy -= cut_y
                            fr.write(str(yy) + " " + ln[1] + "\n")
                        ct += 1
