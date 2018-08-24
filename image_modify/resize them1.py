import cv2
import os

path = "./google-hip bone x ray-107/"
i = 0
for a, b, dirs in os.walk(path):
    for filename in dirs:
        i += 1
        img0 = cv2.imread(path + filename, 0)
        print(path + filename)
        if img0 is None:
            # print("1")
            continue
        x = img0.shape[0]
        y = img0.shape[1]
        print("wid = %d  height = %d" % (x, y))
        f1 = "%d_gooh.jpeg" % i
        res = img0
        if x < 150:
            res = cv2.resize(img0, None, fx=4.1, fy=4.1, interpolation=cv2.INTER_CUBIC)
        elif x < 200:
            res = cv2.resize(img0, None, fx=3.3, fy=3.3, interpolation=cv2.INTER_CUBIC)
        elif x < 240:
            res = cv2.resize(img0, None, fx=2.7, fy=2.7, interpolation=cv2.INTER_CUBIC)
        elif x < 300:
            res = cv2.resize(img0, None, fx=2.33, fy=2.33, interpolation=cv2.INTER_CUBIC)
        elif x < 350:
            res = cv2.resize(img0, None, fx=1.9, fy=1.9, interpolation=cv2.INTER_CUBIC)
        elif x < 400:
            res = cv2.resize(img0, None, fx=1.7, fy=1.7, interpolation=cv2.INTER_CUBIC)
        elif x < 480:
            res = cv2.resize(img0, None, fx=1.4, fy=1.4, interpolation=cv2.INTER_CUBIC)
        elif x < 550:
            res = cv2.resize(img0, None, fx=1.2, fy=1.2, interpolation=cv2.INTER_CUBIC)
        elif x > 2700:
            res = cv2.resize(img0, None, fx=0.19, fy=0.19, interpolation=cv2.INTER_CUBIC)
        elif x > 2200:
            res = cv2.resize(img0, None, fx=0.22, fy=0.22, interpolation=cv2.INTER_CUBIC)
        elif x > 1800:
            res = cv2.resize(img0, None, fx=0.27, fy=0.27, interpolation=cv2.INTER_CUBIC)
        elif x > 1500:
            res = cv2.resize(img0, None, fx=0.33, fy=0.33, interpolation=cv2.INTER_CUBIC)
        elif x > 1200:
            res = cv2.resize(img0, None, fx=0.41, fy=0.41, interpolation=cv2.INTER_CUBIC)
        elif x > 970:
            res = cv2.resize(img0, None, fx=0.51, fy=0.51, interpolation=cv2.INTER_CUBIC)
        elif x > 800:
            res = cv2.resize(img0, None, fx=0.62, fy=0.62, interpolation=cv2.INTER_CUBIC)
        elif x > 650:
            res = cv2.resize(img0, None, fx=0.76, fy=0.76, interpolation=cv2.INTER_CUBIC)
        cv2.imwrite("./google-hip bone x ray resize-107/%s" % f1, res)
        # cv2.imshow("to%d" % i, res)
        # cv2.waitKey(0)




