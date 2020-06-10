class Coin:
    def __init__(self, money=0.0, number=0):
        self.__nominal = money
        self.__ilosc = number

    def __str__(self):
        text = ""
        text += f'{str(self.__nominal)} ilość : {str(self.__ilosc)}'
        return text

    def wartosc(self):
        return round(self.__nominal * self.__ilosc, 2)

    def get_nominal(self):
        return round(self.__nominal, 2)

    def get_ilosc(self):
        return self.__ilosc

    def inc(self):
        self.__ilosc += 1

    def dec(self):
        self.__ilosc -= 1
