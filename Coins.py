class Coin:
    def __init__(self, nominal=0.0, amount=0):
        self.__nominal = nominal
        self.__amount = amount

    def __str__(self):
        text = ""
        text += f'{str(self.__nominal)} ilość : {str(self.__amount)}'
        return text

    def value(self):
        return round(self.__nominal * self.__amount, 2)

    def get_nominal(self):
        return round(self.__nominal, 2)

    def get_amount(self):
        return self.__amount

    def increment_amount(self):
        self.__amount += 1

    def decrement_amount(self):
        self.__amount -= 1
