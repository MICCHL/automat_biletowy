import tkinter as tk

from Give_Back import GiveBackFrame
from payment_frame import PaymentFrame

from Ticket import Ticket
from colour import Colour
from constant import Constants
from ticket_name import TicketNames
from payment_service import PaymentService


class Machine(tk.Frame):
    PAY = "Zapłać"
    GIVE_BACK_COINS = "Zwróć monety"
    PURCHASE = "KUP"
    TAKE_REST = "Zabierz reszte"
    START_AGAIN = "Od początku"
    BACK = "Wróć"

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.parent = parent

        self.ticket = []
        self.screen = []
        self.screen = tk.Text()
        self.text = "Kup Bilet"

        self.payment_service = PaymentService()
        self.buy_ticket = []

        self.init_tickets()
        self.create_widgets()
        self.center()

    def create_widgets(self):

        self.parent.title(Constants.MAIN_FRAME_TITLE)
        self.pack(fill=tk.X, expand=True)

        left_frame = tk.Frame(self)
        left_frame.pack(side=tk.LEFT, fill=tk.Y)
        side_frame = tk.Frame(self)
        side_frame.pack(side=tk.RIGHT, fill=tk.Y)

        for i, name in enumerate(TicketNames):
            ticket = tk.Button(left_frame, text=name,
                               height=Constants.BUTTON_HEIGHT, width=Constants.BUTTON_WIDTH,
                               bg=Constants.COLOUR, overrelief=tk.SUNKEN,
                               command=lambda i=i: self.add_ticket(i))

            ticket.pack(fill=tk.Y, anchor=tk.N)

        self.screen = tk.Text(side_frame, width=Constants.BUTTON_WIDTH, height=10, wrap=tk.WORD)
        self.screen.pack(fill=tk.Y, anchor=tk.N)
        self.screen.insert(0.0, f'Nazwa: {self.text} \nKwota:{self.payment_service.get_ticket_cost()}'
                                f' \nWrzucono:{self.payment_service.user_balance}')

        self.init_menu_buttons(side_frame)

    def init_menu_buttons(self, side_frame):
        throw_coin_button = tk.Button(side_frame, text=Machine.PAY,
                                      width=Constants.BUTTON_WIDTH, height=4,
                                      background=Colour.GREEN, overrelief=tk.SUNKEN,
                                      command=self.throw_coins)

        throw_coin_button.pack(fill=tk.Y, anchor=tk.N)

        give_back_coins_button = tk.Button(side_frame, text=Machine.GIVE_BACK_COINS,
                                           width=Constants.BUTTON_WIDTH, height=4,
                                           bg=Colour.RED, overrelief=tk.SUNKEN,
                                           command=self.get_back_coins)

        give_back_coins_button.pack(fill=tk.Y, anchor=tk.N)

        purchase_button = tk.Button(side_frame, text=Machine.PURCHASE,
                                    width=Constants.BUTTON_WIDTH, height=4,
                                    bg=Colour.WHITE, overrelief=tk.SUNKEN,
                                    command=lambda: self.purchase_ticket())

        purchase_button.pack(fill=tk.Y, anchor=tk.N)

        take_rest_button = tk.Button(side_frame, text=Machine.TAKE_REST,
                                     width=Constants.BUTTON_WIDTH, height=2,
                                     bg=Colour.GREY, overrelief=tk.SUNKEN,
                                     command=self.take_coins)

        take_rest_button.pack(fill=tk.Y, anchor=tk.N)

        start_again = tk.Button(side_frame, text=Machine.START_AGAIN,
                                width=Constants.BUTTON_WIDTH, height=2,
                                bg=Colour.GREY, overrelief=tk.SUNKEN,
                                command=lambda: self.start_again())

        start_again.pack(fill=tk.Y, anchor=tk.N)

    def center(self):
        self.master.update_idletasks()
        width = self.master.winfo_width()
        height = self.master.winfo_height()
        center_x = (self.master.winfo_screenwidth() // 2) - (width // 2)
        center_y = (self.master.winfo_screenheight() // 2) - (height // 2)
        self.master.geometry('{}x{}+{}+{}'.format(width, height, center_x, center_y))

    def init_tickets(self):

        self.ticket = [Ticket(name=Constants.TICKET_NAMES[x], price=Constants.TICKET_PRICES[x])
                       for x in range(6)]

    def throw_coins(self):

        pocket = tk.Tk()
        pocket.title(Constants.PAYMENT_TITLE)
        PaymentFrame(pocket, self.payment_service)
        pocket.mainloop()

        if self.payment_service.is_coin_inside():
            self.write(f'Nazwa: {self.text}  \nKwota: {self.payment_service.get_ticket_cost()}'
                       f'\nWrzucono: {self.payment_service.user_balance}')

    def get_back_coins(self):
        self.payment_service.get_back_coins()
        self.screen.delete(0.0, tk.END)
        self.screen.insert(0.0, f'Nazwa: {self.text} \nKwota: '
                                f'{self.payment_service.get_ticket_cost()} '
                                f'\nWrzucono: {self.payment_service.user_balance}')

    def take_product(self):

        prod = tk.Tk()
        prod.title("Zabierz bilety ")
        GiveBackFrame(prod, self.buy_ticket, "Twoje bilety ")
        prod.mainloop()
        self.buy_ticket = []
        self.write(
            f'Nazwa: {self.text} \nKwota: {self.payment_service.get_ticket_cost()} '
            f'\nWrzucono:{self.payment_service.user_balance}')

    def add_ticket(self, key):
        obj = ""
        if 0 <= key <= 5:
            change = key
            for i in self.ticket:
                if change == i.get_product_id():
                    obj = i

            coin = obj.get_price()
            if coin != 0.0:
                self.payment_service.ticket_cost += coin
                self.text += "\n" + str(obj.get_name())
                self.buy_ticket.append(obj.get_name())
                self.write(f'Nazwa: {self.text} \nKwota: {self.payment_service.get_ticket_cost()}'
                           f' \nWrzucono: {self.payment_service.user_balance}')

        elif self.text == "":
            self.write("Nie wybrałeś biletu ")
            self.text = ""

    def start_again(self):
        self.text = ""
        self.payment_service.ticket_cost = 0.0
        self.buy_ticket = []
        self.write(f'Nazwa: {self.text} \nKwota: {self.payment_service.get_ticket_cost()}'
                   f' \nWrzucono: {self.payment_service.user_balance}')

    def purchase_ticket(self):
        if not self.text == "" and self.buy_ticket:
            if self.payment_service.is_enough_money():
                if self.payment_service.purchase_tickets():
                    self.text = ""
                    self.write(f'Nazwa: {self.text} '
                               f'\nKwota: {self.payment_service.get_ticket_cost()}'
                               f'\nWrzucono: {self.payment_service.user_balance} '
                               f'\nZabierz resztę ')
                    self.payment_service.clear_users_data()
                    self.take_product()
                else:
                    self.payment_service.get_back_coins()
                    self.text = ""
                    self.write("Wrzuć odliczoną kwotę \nWybierz ponownie ")
            else:
                self.write("Za mało pieniędzy \nWybierz ponownie ")
                self.text = ""
        else:
            self.write("Nie wybrałeś biletu ")
            self.text = ""

    def take_coins(self):
        mach = tk.Tk()
        mach.title("Zabierz RESZTĘ ")
        GiveBackFrame(mach, self.payment_service.rest_coins, "Twoja reszta")
        mach.mainloop()
        self.text = ""
        self.write(f'Nazwa: {self.text} \nKwota: {self.payment_service.get_ticket_cost()} '
                   f'\nWrzucono: {self.payment_service.user_balance}')

    def write(self, text):

        self.screen.delete(0.0, tk.END)
        self.screen.insert(0.0, text)
