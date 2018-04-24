import random
from tkinter import *
from PIL import Image, ImageTk
at = Tk()
at.title("Foto Albüm")
at.geometry("800x650")

foto1 = ImageTk.PhotoImage(Image.open("foto1.jpg"))
foto2 = ImageTk.PhotoImage(Image.open("foto2.jpg"))

etiket = Label(at, text="FOTO ALBÜM")
etiket.pack()

def ileri():
    if display == foto1:
        panel1.configure(image=foto2)
    else:
        panel1.configure(image=foto1)

ileributon = Button(at, text=">", command=ileri)
ileributon.pack(side="right")

def geri():
    if display2 == foto2:
        panel1.configure(image = foto1)
    else:
        panel1.configure(image = foto2)

geributon = Button(at, text="<", command=geri)
geributon.pack(side="left")

panel1 = Label(at, image=foto1)
display = foto1
panel1.pack(side="top")

panel2 = Label(at, image=foto2)
display2 = foto2

def çıkış():
    etiket['text'] = "Görüşmek Üzere"
    ileributon['state'] = "disabled"
    geributon['state'] = "disabled"
    at.after(1000, at.destroy)

cikis = Button(at, text="Çıkış", command=çıkış)
cikis.pack()

at.mainloop()
