import cv2
import numpy as np
import os

path = "./xxx/"
i = 0
for a, b, dirs in os.walk(path):
    for filename in dirs:
        i += 1
        img0 = cv2.imread(path + filename)
        if img0 is None:
            continue
        x = img0.shape[0]
        y = img0.shape[1]
        print("wid = %d  height = %d" % (x, y))
        cropped1 = img0[0:x, 0:(y >> 1)]
        cropped2 = img0[0:x, (y >> 1):y]
        f1 = "%d_lf.jpeg" % i
        f2 = "%d_ri.jpeg" % i
        cp1 = cropped1
        cp2 = cropped2
        if x < 320:
            cp1 = cv2.resize(cropped1, None, fx=2, fy=2, interpolation = cv2.INTER_CUBIC)
            cp2 = cv2.resize(cropped2, None, fx=2, fy=2, interpolation = cv2.INTER_CUBIC)
        elif x < 400:
            cp1 = cv2.resize(cropped1, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)
            cp2 = cv2.resize(cropped2, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)
        cv2.imwrite("./xxxcropped/%s" % f1, cp1)
        cv2.imwrite("./xxxcropped/%s" % f2, cp2)
        # cv2.imshow("to%d" % i, cp1)
        # cv2.imshow("fo%d" % i, cp2)
        # cv2.waitKey(0)


# img0 = cv2.imread("001.jpg")
# x = img0.shape[0]
# y = img0.shape[1]
# print("wid = %d  height = %d" % (x, y))
# cropped = img0[0:x, 0:(y>>1)]
# cv2.imshow("to", cropped)
# cv2.waitKey(0)




