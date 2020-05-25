
class Ticket:
    count=0
    def __init__(self, name = "", prize = 0.0):
        self.__nazwa = name
        self.__cena = prize
        self.__nr_produktu = Ticket.count
        Ticket.counting()
    def __str__(self):
        text = ""
        text += str(self.__nazwa + " :" + str(self.__cena))
        return text


    @staticmethod
    def counting():
        Ticket.count += 1

    def get_cena(self):

        return self.__cena

    def get_nazwa(self):

        return self.__nazwa

    def get_nr(self):

        return self.__nr_produktu
