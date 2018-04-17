import tkinter as tk
import random
at = tk.Tk()

at.configure(background= "lightblue")
at.geometry("1920x1080")

def siiryazdir():
    siir = ("\n\n Beni bir kere dövdüler çok gözlüklüydüm \n Daha bere giyiyordum bıyıklarım da "
            "duruyor\nBüyükdere’de dövdüler emirgan ve birileri\nGeceleyin dövdüler dişlerimi tükürdüm\n",
            "\n\nBen sana mecburum bilemezsin\n Adını mıh gibi aklımda tutuyorum\nBüyüdükçe büyüyor gözlerin\nBen sana "
            "mecburum bilemezsin\nİçimi seninle ısıtıyorum.\n", "\n\nAysel git başımdan ben sana göre değilim\nÖlümüm birden olacak seziyorum\nHem kötüyüm karanlığım biraz çirkinim\nAysel git başımdan istemiyorum.\n")
    secilen = random.choice(siir)
    siirsec = tk.Label(text = secilen, font=("arial", 35), fg="black", bg="lightblue")
    siirsec.pack()
def çıkış():
    yazı['text'] = "Görüşmek Üzere"
    buton['text'] = "Bekleyin"
    buton2['text'] = ":)"
    buton2['state'] = "disabled"
    buton['state'] = "disabled"
    at.after(1000, at.destroy)

yazı = tk.Label(text = "Beha Öker", font=("times new roman", 50), fg="red", bg="lightblue")
yazı.pack(side="left")

buton = tk.Button(text = "ÇIK", command=çıkış, font=("Monotype Corsiva",75), fg="black", bg="aqua")
buton.pack(side="right")

buton2 =tk.Button(text="Şiir Yazdır", command=siiryazdir, font=("Monotype Corsiva", 100), fg="black", bg="aqua")
buton2.pack(side="top")

at.mainloop()
