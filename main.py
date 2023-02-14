from tkinter import *
from tkinter import messagebox, filedialog
from tkinter.filedialog import askopenfile, asksaveasfile

file_name = NONE

#Функция для нового файла
def new_file():
    global file_name
    file_name = "Без названия"
    text.delete('1.0', END)

#Функция для сохранения
def save_as():
    out = asksaveasfile(mode='w', defaultextension='.json')
    data = text.get('1.0', END)
    try:
        out.write(data.rstrip())
    except Exception:
        messagebox.showerror("Ой!", "Не удалось сохранить файл")

#Функция для открытия
def open_file():
    file_path = filedialog.askopenfilename(title='Выбор файла',
                                           filetypes=(('Текстовые документы (*.json)', '*.json'), ('Все файлы', '*.*')))
    if file_path:
        text.delete('1.0', END)
        text.insert('1.0', open(file_path).read())

#Создание окна
root = Tk()
root.title("Заметки")
root.geometry("400x400")

#Создание текстового поля
text = Text(root, width=400, height=400)
text.pack()

#Создание меню бар
menu_bar = Menu(root)
file_menu = Menu(menu_bar)
menu_bar.add_cascade(label="Файл", menu=file_menu)

file_menu.add_command(label="Новый", command=new_file)
file_menu.add_command(label="Открыть", command=open_file)
file_menu.add_command(label="Сохранить как", command=save_as)

root.config(menu=menu_bar)
root.mainloop()