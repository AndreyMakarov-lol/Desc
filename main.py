from tkinter import *
from tkinter import ttk

# Подсчет количества кликов
clicks = 0
def click_button():
    global clicks
    clicks += 1
    # Изменяем текст в кнопке
    btn1['text'] = f"Кликов {clicks}"
# Надо для отслеживания закрытия приложения
def finish():
    root.destroy()  # ручное закрытие окна и всего приложения
    print("Закрытие приложения")

root = Tk() # Создаем корневой объект

root.title('Моё первое приложение') # Задаем заголовок окна
#root.iconbitmap(file="hyi.ico") # Установка иконки
icon = PhotoImage(file="hyi.png") # Установка иконкой изображения
root.iconphoto(False, icon)
root.geometry("400x400+200+200") # Задаем размер окна + смещение окна относительно левого верхнего угла
#root.update_idletasks() # метод необходим для отображения в обход root.mainloop() размера окна
#print(root.geometry()) # отображение в консоли размера окна и отступов 
#root.resizable(False, False) # запрет изменения размера окна
#root.minsize(100,100) # Минимальный размер окна
#root.maxsize(400,400) # Максимальный размер окна
#root.attributes("-fullscreen", True) # Открыти приложения в полноэкранном режме

lable = Label(text="Хуя себе, смотри что могу") # Создаем текст внутри окна
lable.pack() # размещаем метку в окне
# Создаем кнопку, command=click_button отвечает за выполнение внешней функции
btn1 = ttk.Button(text="Зашифровать", command=click_button) # Для отключения кнопки state=["disabled"]
btn1.pack(fill=X,padx=[100,50], pady=50, ipadx=20, ipady=20) # (expand=True) чтобы элемент занимал все свободное место
# fill для заполнения контейнера BOTH Заполняет все, X и Y свои оси
# anchor расположение элемента по углам и вершинам
# Отступы элемента padxy
root.protocol("WM_DELETE_WINDOW", finish) # перехват закрытия приложения

root.mainloop() # запускаем цикл обработки событий окна
#https://metanit.com/python/tkinter/1.2.php
