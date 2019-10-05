"""Открывает ссылку, хранящуюся в QR коде"""

import cv2 as cv
import webbrowser
import pyzbar.pyzbar as pyzbar
cap = cv.VideoCapture(0)# gets video from web cam

while True:
    _, frame = cap.read()# gets something and a frame

    """Detects QR code with pyzbar"""
    decoded = pyzbar.decode(frame)
    for obj in decoded:
        webbrowser.open(obj.data)
        exit()

    cv.imshow("image", frame)
    key = cv.waitKey(1)# waits for any key
    if key == 13:# if its Enter - breaks the loop
        break