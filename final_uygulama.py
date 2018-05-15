import tkinter
from random import choice
class Simon() :
    def __init__(self, master) :

        self.master = master
        self.master.minsize(640, 480)
        self.master.resizable(False, False)
        self.master.title("Simon Memory Game")
        self.master.update()

        self.gcanvas = tkinter.Canvas(self.master, width = self.master.winfo_width(), height = self.master.winfo_height(), highlightthickness = 0)
        self.gcanvas.pack()

        self.anarenk = ("red", "blue", "green", "yellow")
        self.gecis = ("black", "black", "black", "black")
        self.rrenk = [color for color in self.anarenk]

        self.dortgen = []

        self.sira = [choice(self.anarenk)]
        self.sirayeri = 0

        self.kanvasciz()

        self.siragoster()

        self.master.mainloop()

    def siragoster(self) :
        self.flas(self.sira[self.sirayeri])
        if(self.sirayeri < len(self.sira) - 1) :
            self.sirayeri += 1
            self.master.after(750, self.siragoster)
        else :
            self.sirayeri = 0

    def flas(self, color) :
        index = self.anarenk.index(color)
        if self.rrenk[index] == self.anarenk[index] :
            self.rrenk[index] = self.gecis[index]
            self.master.after(500, self.flas, color)
        else :
            self.rrenk[index] = self.anarenk[index]
        self.kanvasciz()

    def secimisareti(self) :
        color = self.anarenk[self.dortgen.index(self.gcanvas.find_withtag("current")[0])]
        if(color == self.sira[self.sirayeri]) :
            if(self.sirayeri < len(self.sira) - 1) :
                self.sirayeri += 1
            else :
                self.master.title("Simon  - Puan: {}".format(len(self.sira)))
                self.sira.append(choice(self.anarenk))
                self.sirayeri = 0
                self.siragoster()
        else :
            self.master.title("Simon - Oyun Bitti! | Puanın: {}".format(len(self.sira)))
            self.sira[:] = []
            self.sira.append(choice(self.anarenk))
            self.sirayeri = 0
            self.siragoster()

    def kanvasciz(self) :
        self.master.after(250)
        self.dortgen[:] = []
        self.gcanvas.delete("all")
        for index, color in enumerate(self.rrenk) :
            if index <= 1 :
                self.dortgen.append(self.gcanvas.create_rectangle(index * self.master.winfo_width(), 0, self.master.winfo_width() / 2, self.master.winfo_height() / 2, fill = color, outline = color))
            else :
                self.dortgen.append(self.gcanvas.create_rectangle((index - 2) * self.master.winfo_width(), self.master.winfo_height(), self.master.winfo_width() / 2, self.master.winfo_height() / 2, fill = color, outline = color))
        for id in self.dortgen :
            self.gcanvas.tag_bind(id, '<ButtonPress-1>', lambda e : self.secimisareti())

def main() :
    root = tkinter.Tk()
    gui = Simon(root)

if __name__ == "__main__" : main()
