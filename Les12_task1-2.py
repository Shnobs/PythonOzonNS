from tkinter import *
from tkinter.filedialog import *
import json

root = Tk()  # Создаем объект класса Tk из библиотеки tkinter
root.title('Notepad+')  # Имя приложения
root.geometry('1280x720')  # Размер окна
root.resizable(width=False, height=False)  # Запрет на иизменение размеров окна

frame_bottom = Frame(root)  # Пустой фрейм снизу, для размещения кнопок кнопок
frame_top = Frame(root)  # Пустой фрейм сверху для текстового поля
# Значение WORD опции wrap позволяет переносить слова на новую строку целиком, добавлен цвет заливки #bce2eb
text = Text(frame_top, width=158, height=43, bg="#bce2eb", wrap=WORD)
scroll = Scrollbar(frame_top, orient=VERTICAL, command=text.yview)  # Привязывается прокрутка текстового поля по оси y
text.configure(yscrollcommand=scroll.set)  # Текстовому полю устанавливается ранее созданный скроллер
#  Упаковываем в приложении фреймы и поле растягиваем их по осям
frame_top.pack(side=TOP, fill=X)
frame_bottom.pack(side=BOTTOM, fill=X)
scroll.pack(side=RIGHT, fill=Y)
text.pack(side=LEFT, fill=BOTH)


def open_command():  # Функция открытия файла с любым допустимым расширением
    file = Open(root, filetypes=[("All Files", "*.*")]).show()  # Метод  show вернёт строку с именем или пустую строку
    if file == '':
        return
    text.delete('1.0', 'end')  # Очищаем текстовое поле при открытие нового файла
    text.insert('1.0', open(file, 'rt', encoding='utf-8').read())  # Вставляем в поле text данные из открытого файла


def save_command():  # Функция сохранения данных из текстового поля в файл
    file = SaveAs(root, initialfile='Untitled.txt', filetypes=[('*.txt files', '.txt')]).show()
    if file == '':
        return
    if not file.endswith(".txt"):  # Проверяем расширение файла
        file += ".txt"  # Добавляем расширение .txt
    open(file, 'wt').write(text.get('1.0', 'end'))  # Задаем индексы начала и конца текста в поле
    with open('setting.json', 'w') as filejson:  # Дополнительно открываем json-файл для записи
        data = {'file_name': file}
        json.dump(data, filejson)  # Записываем путь к файлу в json-файл


def start_command():  # Функция получения данных из json-файла, запускается при старте программы
    with open('setting.json', 'r') as filejson:
        fjs = json.load(filejson)  # Загружаем данные из json-файла, на выходе получаем словарь
        text.delete('1.0', 'end')  # Очищаем текстовое поле при открытие нового файла
        text.insert('1.0', open(f'{fjs["file_name"]}', 'rt', encoding='utf-8').read())  # Открытие пути, сохраненного в файле json


save_button = Button(frame_bottom, text='Сохранить', width=10, height=1, command=save_command)
open_button = Button(frame_bottom, text='Загрузить', width=10, height=1, command=open_command)
save_button.pack(side=RIGHT, anchor=SW)  # Упаковываем в нижнем фрейме, ставим якорь (anchor) на ЮЗ угол
open_button.pack(side=LEFT, anchor=SE)  # Упаковываем в нижнем фрейме, ставим якорь (anchor) на ЮВ угол

start_command()  # Запуск функцию считывания данных из json-файла
root.mainloop()
