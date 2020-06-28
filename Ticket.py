class Ticket:
    count = 0

    def __init__(self, name="", price=0.0):
        self.__name = name
        self.__price = price
        self.__product_id = Ticket.count
        Ticket.generate_id()

    def __str__(self):
        text = ""
        text += f'{self.__name} :{self.__price}'
        return text

    @staticmethod
    def generate_id():
        Ticket.count += 1

    def get_price(self):
        return self.__price

    def get_name(self):
        return self.__name

    def get_product_id(self):
        return self.__product_id
