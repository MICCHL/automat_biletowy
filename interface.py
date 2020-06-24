import tkinter as tk

from Give_Back import Give_Back
from Throwing_coins import Throwing_coins
from Coins import Coin

from Ticket import Ticket

SZEROKOSC = 25
WYSOKOSC = 5
KOLOR = '#9F9FDF'
TEN = 10
ELEVEN = 11
NOMINAL = [50.0, 20.0, 10.0, 5.0, 2.0, 1.0, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]
ILOSC = [3, 5, 4, 0, 12, 0, 14, 0, 4, 0, 55, 100]



class Maschine (tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.parent = parent

        self.ticket = []
        self.choose_ticket = []
        self.sum_coins = 0.0
        self.sum_ticket = 0.0

        self.text = "Kup Bilet"

        self.monety_wrzucane = []
        self.reszta = 0.0
        self.money_in_maschine = []
        self.sum_in_maschine = 0.0
        self.money_rest = []

        self.buy_ticket = []

        self.inicjalize_coins()
        self.inicjalize_ticket()
        self.create_widgets()
        self.center()

    def create_widgets(self):

        self.parent.title("Automat biletowy MPK")
        self.pack(fill=tk.X, expand=True)

        left_frame = tk.Frame(self)
        left_frame.pack(side=tk.LEFT, fill=tk.Y)
        side_frame = tk.Frame(self)
        side_frame.pack(side=tk.RIGHT, fill=tk.Y)

        nazwy_biletów = [
            'Bilet normalny 20 min\n3,40 zł',
            'Bilet ulgowy 20 min\n1,70 zł',
            'Bilet normalny 50 min \n4,60zł',
            'Bilet ulgowy 50 min\n2, 30zł',
            'Bilet normalny 90 min\n6zł',
            'Bilet ulgowy 90 min\n3zł'
        ]

        k_bilety = []

        for i, nazwa in enumerate(nazwy_biletów):

            bilet = tk.Button(left_frame, text=nazwa,
                          height=WYSOKOSC, width=SZEROKOSC,
                           bg=KOLOR, overrelief=tk.SUNKEN,
                          command=lambda i=i: self.keys_operation(i))

            bilet.pack(fill=tk.Y, anchor=tk.N)

            k_bilety.append(bilet)

        self.screen = tk.Text(side_frame, width=SZEROKOSC, height=10, wrap=tk.WORD)
        self.screen.pack(fill=tk.Y, anchor=tk.N)
        self.screen.insert(0.0, f'Nazwa: {self.text} \nKwota:{self.sum_ticket}'
                                f' \nWrzucono:{self.sum_coins}')

        key_wrzuc = tk.Button(side_frame, text="Zapłać", width=SZEROKOSC, height=4,
                           bg="#55A41C", overrelief=tk.SUNKEN,
                           command=self.throw_coins)
        key_wrzuc.pack(fill=tk.Y, anchor=tk.N)

        key_oddaj = tk.Button(side_frame, text="Zwróć monety", width=SZEROKOSC, height=4,
                           bg="#C91F16", overrelief=tk.SUNKEN,
                           command=self.g_b_coins)
        key_oddaj.pack(fill=tk.Y, anchor=tk.N)

        key_kup = tk.Button(side_frame, text="KUP", width=SZEROKOSC, height=4,
                         bg="white", overrelief=tk.SUNKEN,
                         command=lambda: self.keys_operation(11))
        key_kup.pack(fill=tk.Y, anchor=tk.N)

        key_oddaj = tk.Button(side_frame, text="Zabierz reszte",
                           width=SZEROKOSC, height=2, bg="#A7A7A7",
                           overrelief=tk.SUNKEN,
                           command=self.take_coins)
        key_oddaj.pack(fill=tk.Y, anchor=tk.N)

        key_cofnij = tk.Button(side_frame, text="Od początku", width=SZEROKOSC,
                            height=2, bg="#A7A7A7", overrelief=tk.SUNKEN,
                            command=lambda: self.keys_operation(10))
        key_cofnij.pack(fill=tk.Y, anchor=tk.N)

    def center(self):
        self.master.update_idletasks()
        width = self.master.winfo_width()
        height = self.master.winfo_height()
        x = (self.master.winfo_screenwidth() // 2) - (width // 2)
        y = (self.master.winfo_screenheight() // 2) - (height // 2)
        self.master.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    def inicjalize_coins(self):

        self.money_in_maschine = [Coin(money=NOMINAL[x], number=ILOSC[x])
                                  for x in range(12)]

    def inicjalize_ticket(self):

        nazwy = ["Normalny 20 min", "Ulgowy 20 min", "Normalny 50 min ",
                 "Ulgowy 50 min ", "Normalny 90 min", "Ulgowy 90 min"]
        cena = [3.40, 1.70, 4.6, 2.30, 6, 3]

        self.ticket = [Ticket(name=nazwy[x], prize=cena[x]) for x in range(6)]

    def throw_coins(self):

        pocket = tk.Tk()
        pocket.title("Portfel")
        pckt = Throwing_coins(pocket)
        pocket.mainloop()

        moneta = pckt.get_coin()
        if moneta != 0.0:
            self.sum_coins += moneta
            self.sum_coins = round(self.sum_coins, 2)
            self.monety_wrzucane.append(moneta)
            self.write(f'Nazwa: {self.text}  \nKwota: {self.sum_ticket}'
                       f'\nWrzucono: {self.sum_coins}')

    def g_b_coins(self):

        self.money_rest = [x for x in self.monety_wrzucane]
        print("zwrócone :", self.money_rest)
        self.monety_wrzucane = []
        self.sum_coins = 0.0
        self.screen.delete(0.0, tk.END)
        self.screen.insert(0.0, f'Nazwa: {self.text} \nKwota: '
                                f'{self.sum_ticket} '
                                f'\nWrzucono: {self.sum_coins}')

    def take_coins(self):

        print("reszta :", self.money_rest)
        mach = tk.Tk()
        mach.title("Zabierz RESZTĘ!")
        gbc = Give_Back(mach, self.money_rest, "Twoja reszta")
        mach.mainloop()
        self.money_rest = []
        self.text = ""
        self.sum_ticket = 0.0
        self.write(f'Nazwa:{self.text}  \nKwota: {self.sum_ticket}'
                   f'  \nWrzucono: {self.sum_coins}')

    def take_product(self):

        prod = tk.Tk()
        prod.title("Zabierz bilety ")
        gbc = Give_Back(prod, self.buy_ticket, "Twoje bilety ")
        prod.mainloop()
        self.buy_ticket = []
        self.write(f'Nazwa: {self.text} \nKwota: {self.sum_ticket} \nWrzucono:{self.sum_coins}')

    def rest(self, ticket):

        for j in self.monety_wrzucane:
            for k in self.money_in_maschine:
                if j == k.get_nominal():
                    k.inc()

        for i in self.money_in_maschine:
            self.sum_in_maschine += i.wartosc()
        self.sum_in_maschine = round(self.sum_in_maschine, 2)

        for obj in self.money_in_maschine:
            print(obj)
            print("-------")

        if self.reszta < self.sum_in_maschine:

            for i in self.money_in_maschine:
                logic = True
                while logic:
                    if (round(self.reszta, 2) - i.get_nominal() >= 0) \
                            and (i.get_ilosc() > 0):
                        self.money_rest.append(i.get_nominal())
                        self.reszta -= i.get_nominal()
                        self.reszta = round(self.reszta, 2)
                        i.dec()
                    else:
                        logic = False
                if self.reszta == 0.0:
                    break

            if self.reszta == 0.0:
                self.monety_wrzucone = []
                self.sum_coins = 0.0
                self.sum_ticket = 0.0
                self.take_product()
                self.text = ""
                self.write(f'Nazwa: {self.text} \nKwota: {self.sum_ticket}'
                           f' \nWrzucono: {self.sum_coins} \nZabierz resztę ')
            else:
                for j in self.money_rest:
                    for k in self.money_in_maschine:
                        if j == k.get_nominal():
                            k.inc()

                for j in self.monety_wrzucane:
                    for k in self.money_in_maschine:
                        if j == k.get_nominal():
                            k.dec()

                print("reszta :", self.money_rest)
                self.money_rest = [x for x in self.monety_wrzucane]
                self.monety_wrzucane = []
                self.sum_coins = 0.0
                self.text = ""
                self.write("Wrzuć odliczoną kwotę \nWybierz ponownie ")

    def keys_operation(self, key):

        if key == TEN:
            self.choose_ticket = []
            self.text = ""
            self.sum_ticket = 0.0
            self.buy_ticket = []
            self.write(f'Nazwa: {self.text} \nKwota: {self.sum_ticket}'
                       f' \nWrzucono: {self.sum_coins}')

        obj = ""
        if (key >= 0) and (key <= 5):
            change = key
            for i in self.ticket:
                if change == i.get_nr():
                    obj = i

            moneta = obj.get_cena()
            print(moneta)
            if moneta != 0.0:
                self.sum_ticket += moneta
                self.sum_ticket = round(self.sum_ticket, 2)
                print(self.sum_ticket)
                self.text += "\n" + str(obj.get_nazwa())
                self.buy_ticket.append(obj.get_nazwa())
                self.write(f'Nazwa: {self.text} \nKwota: {self.sum_ticket}'
                           f' \nWrzucono: {self.sum_coins}')

        if key == ELEVEN and not self.text == "":
            if self.sum_coins > self.sum_ticket:
                self.reszta = self.sum_coins - self.sum_ticket
                print("Reszta :", self.reszta)
                self.rest(obj)

            elif self.sum_coins == self.sum_ticket:
                self.reszta = 0.0
                self.sum_coins = 0.0

                for i in self.monety_wrzucane:
                    for j in self.money_in_maschine:
                        if i == j.get_nominal():
                            j.inc()

                self.monety_wrzucane = []
                self.text = ""
                self.write(f'Nazwa: {self.text} \nKwota: {self.sum_ticket}'
                           f' \nWrzucono: {self.sum_coins}')
                self.take_product()
            else:
                self.write("Za mało pieniędzy \nWybierz ponownie ")
                self.text = ""

        elif self.text == "":
            self.write("Nie wybrałeś biletu ")
            self.text = ""

    def take_coins(self):
        print("reszta :", self.money_rest)
        mach = tk.Tk()
        mach.title("Zabierz RESZTĘ ")
        gbc = Give_Back(mach, self.money_rest, "Twoja reszta")
        mach.mainloop()
        self.money_rest = []
        self.text = ""
        self.write(f'Nazwa: {self.text} \nKwota: {self.sum_ticket} '
                   f'\nWrzucono: {self.sum_coins}')

    def take_ticket(self):

        prod = tk.Tk()
        prod.title("Odbierz bilet")
        gbc = Give_Back(prod, self.kupione_bilety, "Twoje bilety ")
        prod.mainloop()
        self.kupione_bilety = []
        self.text = ""
        self.write(f'Nazwa: {self.text} \nKwota: {self.sum_ticket} \nWrzucono:{self.sum_coins}')

    def write(self, text):

        self.screen.delete(0.0, tk.END)
        self.screen.insert(0.0, text)

