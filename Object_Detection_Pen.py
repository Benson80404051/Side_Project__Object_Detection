import cv2
import numpy as np

v = cv2.VideoCapture('h3.mp4')

while v.isOpened():
    a, b = v.read()  # a:T/F b:variable for the video
    if a:
        m2 = cv2.inRange(b, (60, 30, 10), (255, 255, 50))  # 範圍內白色, 範圍外黑
        m2 = cv2.dilate(m2, np.ones(40))  # 彩值高侵蝕低
        m2 = cv2.blur(m2, (35, 15))
        m2 = cv2.erode(m2, np.ones(40))  # 彩值低侵蝕高
        c, d = cv2.findContours(m2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)  # arg2=儲存最外層, arg3=存所有輪廓
        if len(c):
            for i in range(0, len(d)):
                x, y, w, h = cv2.boundingRect(c[i])
                cv2.rectangle(b, (x, y), (x + w, y + h), (150, 255, 00), 2)
                cv2.imshow('Object Capture', b)
                k = cv2.waitKey(30)
            if k == 27:
                break
    else:
        break

cv2.destroyAllWindows()
