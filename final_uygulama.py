import tkinter
from random import choice
class Simon() :
    def __init__(self, master) :

        self.master = master
        self.master.geometry("640x480")
        self.master.title("Simon")
        self.master.update()
        self.master.after(100)

        self.game_canvas = tkinter.Canvas(self.master, width = self.master.winfo_width(), height = self.master.winfo_height(), highlightthickness = 1)
        self.game_canvas.pack()

        self.idle_colors = ("red", "blue", "green", "yellow")
        self.tinted_colors = ("black", "black", "black", "black")
        self.current_colors = [color for color in self.idle_colors]

        self.rectangle_ids = []

        self.sequence = [choice(self.idle_colors)]
        self.sequence_position = 0

        self.draw_canvas()

        self.show_sequence()

        self.master.mainloop()

    def show_sequence(self) :
        self.flash(self.sequence[self.sequence_position])
        if(self.sequence_position < len(self.sequence) - 1) :
            self.sequence_position += 1
            self.master.after(750, self.show_sequence)
        else :
            self.sequence_position = 0

    def flash(self, color) :
        index = self.idle_colors.index(color)
        if self.current_colors[index] == self.idle_colors[index] :
            self.current_colors[index] = self.tinted_colors[index]
            self.master.after(450, self.flash, color)
        else :
            self.current_colors[index] = self.idle_colors[index]
        self.draw_canvas()

    def check_choice(self) :
        color = self.idle_colors[self.rectangle_ids.index(self.game_canvas.find_withtag("current")[0])]
        if(color == self.sequence[self.sequence_position]) :
            if(self.sequence_position < len(self.sequence) - 1) :
                self.sequence_position += 1
            else :
                self.master.title("Simon  - Puan: {}".format(len(self.sequence)))
                self.sequence.append(choice(self.idle_colors))
                self.sequence_position = 0
                self.show_sequence()
        else :
            self.master.title("Simon - Oyun Bitti! | Puanın: {}".format(len(self.sequence)))
            self.sequence[:] = []
            self.sequence.append(choice(self.idle_colors))
            self.sequence_position = 0
            self.show_sequence()

    def draw_canvas(self) :
        self.master.after(400)
        self.rectangle_ids[:] = []
        self.game_canvas.delete("all")
        for index, color in enumerate(self.current_colors) :
            if index <= 1 :
                self.rectangle_ids.append(self.game_canvas.create_rectangle(index * self.master.winfo_width(), 0, self.master.winfo_width() / 2, self.master.winfo_height() / 2, fill = color, outline = color))
            else :
                self.rectangle_ids.append(self.game_canvas.create_rectangle((index - 2) * self.master.winfo_width(), self.master.winfo_height(), self.master.winfo_width() / 2, self.master.winfo_height() / 2, fill = color, outline = color))
        for id in self.rectangle_ids :
            self.game_canvas.tag_bind(id, '<ButtonPress-1>', lambda e : self.check_choice())

def main() :
    root = tkinter.Tk()
    gui = Simon(root)

if __name__ == "__main__" : main()