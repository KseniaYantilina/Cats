from cProfile import label
from http.client import responses
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import requests
from io import BytesIO

Allowed_tags = ["sleep","jump","fight","black","white","bengal",
                "siamese","cute","red","big","green", "pink", "newyear", "lol"]

def load_image(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        image_data = BytesIO(response.content)
        img = Image.open(image_data)
        img.thumbnail((600, 480), Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None

def open_new_window():
    tag = tag_combobox.get()
    url_tag = f"http://cataas.com/cat/{tag}" if tag else "http://cataas.com/cat"
    img = load_image(url_tag)

    if img:
        new_window = Toplevel()
        new_window.title("Картинка котика")
        new_window.geometry("600x480")
        label = Label(new_window, image=img)
        label.pack()
        label.image = img

def open_new_window2():
    tag = tag_combobox.get()
    url_tag = "http://cataas.com/cat"
    img = load_image(url_tag)

    if img:
        new_window = Toplevel()
        new_window.title("Картинка котика")
        new_window.geometry("600x480")
        label = Label(new_window, image=img)
        label.pack()
        label.image = img

def exit():
    window.destroy()

window = Tk()
window.title("Cats!")
window.geometry("600x200")

menu_bar = Menu(window)
window.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Файл", menu=file_menu)
file_menu.add_command(label="Загрузить фото", command=open_new_window)
file_menu.add_separator()
file_menu.add_command(label="Выход", command=exit)

url = "http://cataas.com/cat"

frame1 = Frame(window, bg="lightgray", padx=10, pady=10)
frame1.pack()

frame2 = Frame(window, bg="lightgray", padx=10, pady=10)
frame2.pack()

tag_label = Label(frame1, text="Выбери тег")
tag_label.pack(padx=10, side="left")

tag_combobox = ttk.Combobox(frame1, values=Allowed_tags)
tag_combobox.pack(padx=10, side="left")

load_button = Button(frame1, text="Загрузить по тегу", command=open_new_window)
load_button.pack(side="right")

load_button2 = Button(frame2, text="Загрузить случайного котика", command=open_new_window2)
load_button2.pack(side="bottom")



window.mainloop()
