"""
Пользователь подносит к камере QR-код
Распознается лицо пользователя
Распознается QR-код
Изображение лица человека сохраняется в отдельную папку
Проверяется наличие данных в текстовом файле, если они уже есть, то текст НЕ сохраняется снова и
выводиться сообщение о том, что текст уже был сохранен через tkinter !!!
Иначе текстовые данные из QR-кода сохраняются в отдельный файл

"""

from tkinter import *
import cv2 as cv
import pyzbar.pyzbar as pyzbar
import xlsxwriter



"""Распознавание человеческого лица на видео"""
def detect_face(frame):
    faceCascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

    while True:
        """Распознавание лица"""
        faces = faceCascade.detectMultiScale(frame)

        """Синий квадрат около лица"""
        for (x, y, w, h) in faces:
            cv.rectangle(frame, (x, y), (x + w, y + h), (255,0,0), 2)

        return frame



"""Добавляет текст из QR-кода в excel таблицу"""
def add_to_excel_file(filename, dataset):
    workbook = xlsxwriter.Workbook(filename)
    worksheet = workbook.add_worksheet()
    col = 0
    row = 0
    for data in dataset:
        worksheet.write(row, col, data)
        row += 1
    workbook.close()

"""Добавляет текст из QR-кода в текстовый документ"""
def add_to_txt_file(filename, dataset):
    with open(filename, "w") as f:
        for data in dataset:
            f.write(data + "\n")


"""Проверяет наличие текста в текстовом файле"""
def check_if_exists(filename, data):
    with open(filename, "r") as f:
        lines = f.readlines()
        for line in lines:
            line = line[:len(data)]
            if data == line:
                root = Tk()
                text = Text(width = 50, height = 5, bg = "yellow")
                text.insert(1.0, "ERROR: Data in already in the file.\n(press Q to exit)")
                button = Button(root, text = "Got it", command = root.destroy)
                text.pack()
                button.pack()
                root.mainloop()
                return True
        else:
            return False




txt_filename = "text_from_QR.txt"
excel_filename = "table_from_qr.xlsx"
path_to_save = "C:\CREESTL\Programming\PythonCoding\ComputerVision\saved_frames"
video = cv.VideoCapture(0)

dataset = []
i = 0

while True:
    _, frame = video.read()

    """Распознавание лица, возвращает лицо в синем квадрате"""
    detect_face(frame)

    decoded = pyzbar.decode(frame)
    if decoded is not None:
        cv.imshow("smile", frame)

    """Извлечениие чистого текста из QR-кода"""
    for obj in decoded:
        changed_data = str(obj.data)
        changed_data = changed_data.replace("b", "")
        changed_data = changed_data[1:-1]
        if changed_data not in dataset:
            dataset.append(changed_data)
            """Сохранение фотографии лица человека в папку"""
            cv.imwrite("C:\\CREESTL\\Programming\\PythonCoding\\ComputerVision\\saved_frames\\frame" + str(i) + ".jpg",
                       frame)


        in_file = check_if_exists(txt_filename, changed_data)# проверяет, есть ли текст в файле
        if in_file == True:
            pass # если текст уже есть в файле, то ничего не делаем
        else:
            add_to_txt_file(txt_filename, dataset)
            add_to_excel_file(excel_filename, dataset)
            choice = input("QR code has been scanned and added to the file.\nExit the program?(y/n)")
            if choice == "y":
                exit()
            else:
                continue
    i += 1
    key = cv.waitKey(1)
    if key == ord('q'):
        cv.destroyAllWindows()
        exit()



