from tkinter import BOTTOM
from tkinter import Button
from tkinter import Frame
from tkinter import Text
from tkinter import Y


class Give_Back(Frame):
    def __init__(self, master, bc, text):

        super().__init__(master)
        self.typ = text
        self.coins = bc
        self.pack()
        self.create_widgets(master)
        self.center()

    def create_widgets(self, x):

        top_frame = Frame(self)
        top_frame.pack(fill=Y)
        low_frame = Frame(self)
        low_frame.pack(side=BOTTOM, fill=Y)

        self.coins_list = Text(top_frame, width=25, height=20, bg="white")
        self.coins_list.pack()
        self.write_coins()

        self.key1 = Button(low_frame, text="Zabierz", height=3, width=28,
                           background="red", command=lambda: self.back(x))
        self.key1.pack()

    def write_coins(self):

        lista = ""
        lista += self.typ + " :\n"
        for i in self.coins:
            lista += str(i) + "\n"

        self.coins_list.insert(0.0, lista)

    def back(self, x):

        x.quit()
        x.destroy()

    def center(self):
        self.master.update_idletasks()
        width = self.master.winfo_width()
        height = self.master.winfo_height()
        x = (self.master.winfo_screenwidth() // 2) - (width // 2)
        y = (self.master.winfo_screenheight() // 2) - (height // 2)
        self.master.geometry('{}x{}+{}+{}'.format(width, height, x, y))
