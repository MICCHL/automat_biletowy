import tkinter
from colour import Colour
from constant import Constants


class PaymentFrame(tkinter.Frame):
    WIDTH = 15
    HEIGHT = 3
    PAY = "Zapłać"
    BACK = "Wróć"

    def __init__(self, master, payment_service):
        super().__init__(master)
        self.grid()
        self.create_widgets(master)
        self.center()
        self.payment_service = payment_service

    def create_widgets(self, master):
        left_frame = tkinter.Frame(self)
        left_frame.pack(side=tkinter.LEFT, fill=tkinter.Y)
        side_frame = tkinter.Frame(self)
        side_frame.pack(side=tkinter.RIGHT, fill=tkinter.Y)

        label = tkinter.Button(left_frame, text=PaymentFrame.PAY, height=2,
                       width=PaymentFrame.WIDTH, background=Colour.GREY)
        label.pack(fill=tkinter.Y, anchor=tkinter.W)

        for nominal in Constants.NOMINAL:
            nominal_button = tkinter.Button(
                left_frame, text=f'{nominal} zł', height=PaymentFrame.HEIGHT,
                width=PaymentFrame.WIDTH, background=Colour.WHITE,
                command=lambda nominal=nominal: self.throw(nominal, master))
            nominal_button.pack(fill=tkinter.Y, anchor=tkinter.W)

        back_button = tkinter.Button(left_frame, text=PaymentFrame.BACK, height=2,
                             width=PaymentFrame.WIDTH, background=Colour.GREY,
                             command=lambda: self.throw(0.0, master))
        back_button.pack(fill=tkinter.Y, anchor=tkinter.W)

    def throw(self, coin, master):
        self.payment_service.add_coin(coin)
        master.quit()
        master.destroy()

    def center(self):
        self.master.update_idletasks()
        width = self.master.winfo_width()
        height = self.master.winfo_height()
        center_x = (self.master.winfo_screenwidth() // 2) - (width // 2)
        center_y = (self.master.winfo_screenheight() // 2) - (height // 2)
        self.master.geometry('{}x{}+{}+{}'.format(width, height, center_x, center_y))
