from tkinter import Button
from tkinter import Frame
from tkinter import LEFT
from tkinter import RIGHT
from tkinter import W
from tkinter import Y
SZEROKOSC_1 = 15
WYSOKOSC_1 = 3



class Throwing_coins(Frame):
    def __init__(self, master):
        self.__coins = 0.0
        super(Throwing_coins, self).__init__(master)
        self.grid()
        self.create_widgets(master)
        self.center()

    def create_widgets(self, x):
        left_frame = Frame(self)
        left_frame.pack(side=LEFT, fill=Y)
        side_frame = Frame(self)
        side_frame.pack(side=RIGHT, fill=Y)

        self.label = Button(left_frame, text="Zapłać:", height=2,
                            width=SZEROKOSC_1, background="grey")
        self.label.pack(fill=Y, anchor=W)

        self.key1 = Button(left_frame, text="0.01 zł ", height=WYSOKOSC_1,
                           width=SZEROKOSC_1, background="white",
                           command=lambda: self.throw(0.01, x))
        self.key1.pack(fill=Y, anchor=W)

        self.key2 = Button(left_frame, text="0.02 zł", height=WYSOKOSC_1,
                           width=SZEROKOSC_1, background="white",
                           command=lambda: self.throw(0.02, x))
        self.key2.pack(fill=Y, anchor=W)

        self.key3 = Button(left_frame, text="0.05 zł", height=WYSOKOSC_1,
                           width=SZEROKOSC_1, background="white",
                           command=lambda: self.throw(0.05, x))
        self.key3.pack(fill=Y, anchor=W)

        self.key4 = Button(left_frame, text="0.1 zł  ", height=WYSOKOSC_1,
                           width=SZEROKOSC_1, background="white",
                           command=lambda: self.throw(0.1, x))
        self.key4.pack(fill=Y, anchor=W)

        self.key5 = Button(left_frame, text="0.2 zł ", height=WYSOKOSC_1,
                           width=SZEROKOSC_1, background="white",
                           command=lambda: self.throw(0.2, x))
        self.key5.pack(fill=Y, anchor=W)

        self.key6 = Button(left_frame, text="0.5 zł ", height=WYSOKOSC_1,
                           width=SZEROKOSC_1, background="white",
                           command=lambda: self.throw(0.5, x))
        self.key6.pack(fill=Y, anchor=W)

        self.key7 = Button(left_frame, text="1.0 zł  ", height=WYSOKOSC_1,
                           width=SZEROKOSC_1, background="white",
                           command=lambda: self.throw(1.0, x))
        self.key7.pack(fill=Y, anchor=W)

        self.key8 = Button(left_frame, text="2.0 zł ", height=WYSOKOSC_1,
                           width=SZEROKOSC_1, background="white",
                           command=lambda: self.throw(2.0, x))
        self.key8.pack(fill=Y, anchor=W)

        self.key9 = Button(left_frame, text="5.0 zł ", height=WYSOKOSC_1,
                           width=SZEROKOSC_1, background="white",
                           command=lambda: self.throw(5.0, x))
        self.key9.pack(fill=Y, anchor=W)

        self.key9 = Button(left_frame, text="10.0 zł ", height=WYSOKOSC_1,
                           width=SZEROKOSC_1, background="white",
                           command=lambda: self.throw(10.0, x))
        self.key9.pack(fill=Y, anchor=W)

        self.key9 = Button(left_frame, text="20.0 zł ", height=WYSOKOSC_1,
                           width=SZEROKOSC_1, background="white",
                           command=lambda: self.throw(20.0, x))
        self.key9.pack(fill=Y, anchor=W)

        self.key9 = Button(left_frame, text="50.0 zł ", height=WYSOKOSC_1,
                           width=SZEROKOSC_1, background="white",
                           command=lambda: self.throw(50.0, x))
        self.key9.pack(fill=Y, anchor=W)

        self.wroc = Button(left_frame, text="Wróć", height=2,
                           width=SZEROKOSC_1, background="grey",
                           command=lambda: self.throw(0.0, x))
        self.wroc.pack(fill=Y, anchor=W)

    def throw(self, coin, x):
        self.__coins = coin
        x.quit()
        x.destroy()

    def get_coin(self):
        return self.__coins

    def center(self):
        self.master.update_idletasks()
        width = self.master.winfo_width()
        height = self.master.winfo_height()
        x = (self.master.winfo_screenwidth() // 2) - (width // 2)
        y = (self.master.winfo_screenheight() // 2) - (height // 2)
        self.master.geometry('{}x{}+{}+{}'.format(width, height, x, y))
