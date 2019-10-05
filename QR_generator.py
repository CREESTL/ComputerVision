'''
В Excel таблице хранятся данные:
    Имя (столбец 1)
    Фамилия (столбец 2)
    Группа (столбец 3)
Для каждого пользователя создать свой QR-код
Сгенерированные кода помещать в отдельную папку в формате .png



ОБЪЕДИНИТЬ ДВЕ ПРОГИ В ОДНУ, МБ ЧЕРЕЗ ИМПОРТ
'''

import pyqrcode
import pandas
import xlsxwriter


choice = int(input("Хотите ли вы считать данные из существующего файла, или создать новый?(1/2)\n"))
if choice == 1:
    filename = input("Введите имя файла: ")
    data = pandas.read_excel(filename)
    for el in data:
        if type(el) == str:
            qrcode = pyqrcode.create(el)
            '''QR-кода сохраняются в отдельную папку в формате .png'''
            qrcode.png("C:\CREESTL\Programming\PythonCoding\ComputerVision\qr_from_table\ " + el + '.png', scale = 7)
    print("QR-коды успешно сохранены в папку qr_from_table")
elif choice == 2:
    filename = input("Введите имя нового файла для его создния: \n")
    workbook = xlsxwriter.Workbook(filename + ".xlsx")
    worksheet = workbook.add_worksheet()
    row = 0
    col = 0
    while True:
        data = input("Введите слово (для окончания введите '*'): ")
        if data == '*':
            print("Таблице успешно создана!")
            break
        else:
            worksheet.write(row, col, data)
            col += 1

    workbook.close()
















