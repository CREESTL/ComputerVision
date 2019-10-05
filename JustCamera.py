import cv2
import numpy as np

"""Получает изображение с вебки и при нажатии q выходит"""

cap = cv2.VideoCapture(0)# 0 - значит с первой вебки компа

while True:
    ret, frame = cap.read()
    cv2.imshow("frame", frame)# просто показывает картинку

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)#конвертирует все цвета изображения в серый
    cv2.imshow("gray", gray)
    key = cv2.waitKey(1)
    if key == 13:
        break
cap.release()
cv2.destroyAllWindows()


