from tkinter import *

# Надо для отслеживания закрытия приложения
def finish():
    root.destroy()  # ручное закрытие окна и всего приложения
    print("Закрытие приложения")

root = Tk() # Создаем корневой объект

root.title('Моё первое приложение') # Задаем заголовок окна
#root.iconbitmap(file="hyi.ico") # Установка иконки
icon = PhotoImage(file="hyi.png") # Установка иконкой изображения
root.iconphoto(False, icon)
#root.geometry("300x200+200+200") # Задаем размер окна + смещение окна относительно левого верхнего угла
#root.update_idletasks() # метод необходим для отображения в обход root.mainloop() размера окна
#print(root.geometry()) # отображение в консоли размера окна и отступов 
#root.resizable(False, False) # запрет изменения размера окна
#root.minsize(100,100) # Минимальный размер окна
#root.maxsize(400,400) # Максимальный размер окна
#root.attributes("-fullscreen", True) # Открыти приложения в полноэкранном режме

lable = Label(text="Хуя себе, смотри что могу") # Создаем текст внутри окна
lable.pack() # размещаем метку в окне


root.protocol("WM_DELETE_WINDOW", finish) # перехват закрытия приложения

root.mainloop() # запускаем цикл обработки событий окна