import cv2

def detect_face(frame):
    faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    while True:
        """Распознавание лица"""
        faces = faceCascade.detectMultiScale(frame)

        """Синий квадрат около лица"""
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255,0,0), 2)

        return frame


