import tkinter as tk

from colour import Colour


class GiveBackFrame(tk.Frame):
    COINS_LIST_HEIGHT = 20
    COINS_LIST_WIDTH = 25
    TAKE_MONEY_BTN_HEIGHT = 3
    TAKE_MONEY_BTN_WIDTH = 28
    TAKE_MONEY = "Zabierz"

    def __init__(self, master, bc, text):

        super().__init__(master)
        self.typ = text
        self.coins = bc
        self.pack()
        self.create_widgets(master)
        self.center()

    def create_widgets(self, master):

        top_frame = tk.Frame(self)
        top_frame.pack(fill=tk.Y)
        low_frame = tk.Frame(self)
        low_frame.pack(side=tk.BOTTOM, fill=tk.Y)

        coins_list = tk.Text(top_frame, width=GiveBackFrame.COINS_LIST_WIDTH,
                             height=GiveBackFrame.COINS_LIST_HEIGHT, bg=Colour.WHITE)
        coins_list.pack()
        self.write_coins(coins_list)

        take_button = tk.Button(low_frame, text=GiveBackFrame.TAKE_MONEY,
                                height=GiveBackFrame.TAKE_MONEY_BTN_HEIGHT,
                                width=GiveBackFrame.TAKE_MONEY_BTN_WIDTH,
                                background=Colour.RED, command=lambda: self.back(master))
        take_button.pack()

    def write_coins(self, coins_list):

        coins = '\n'.join([f'{self.typ} :'] + [str(c) for c in self.coins])

        coins_list.insert(0.0, coins)

    @staticmethod
    def back(master):
        master.quit()
        master.destroy()

    def center(self):
        self.master.update_idletasks()
        width = self.master.winfo_width()
        height = self.master.winfo_height()
        center_x = (self.master.winfo_screenwidth() // 2) - (width // 2)
        center_y = (self.master.winfo_screenheight() // 2) - (height // 2)
        self.master.geometry('{}x{}+{}+{}'.format(width, height, center_x, center_y))
