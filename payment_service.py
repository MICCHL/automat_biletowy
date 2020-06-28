from Coins import Coin
from constant import Constants


class PaymentService:

    def __init__(self):
        super().__init__()
        self.user_balance = 0.0
        self.ticket_cost = 0.0
        self.user_coins_inside = []
        self.machine_coins = []
        self.init_coins()
        self.rest_coins = []

    def init_coins(self):
        self.machine_coins = [Coin(nominal=Constants.NOMINAL[x], amount=Constants.AMOUNT[x])
                              for x in range(12)]

    def add_coin(self, coin):
        self.user_balance += coin
        self.user_coins_inside.append(coin)

    def is_coin_inside(self):
        return self.user_balance > 0.0

    def get_back_coins(self):
        self.rest_coins = self.user_coins_inside.copy()

        self.user_balance = 0.0
        self.user_coins_inside.clear()

    def purchase_tickets(self):
        result = False
        if self.user_balance > self.ticket_cost:
            rest = self.get_rest()
            if self.can_give_rest(rest):
                self.add_user_coins_to_machine()
                self.withdraw_coins_from_machine(self.rest_coins)
                result = True

        elif self.user_balance == self.ticket_cost:
            self.add_user_coins_to_machine()
            result = True
        return result

    def get_rest(self):
        return round(self.user_balance - self.ticket_cost, 2)

    def add_user_coins_to_machine(self):
        for i in self.user_coins_inside:
            for j in self.machine_coins:
                if i == j.get_nominal():
                    j.increment_amount()
        self.clear_users_data()

    def withdraw_coins_from_machine(self, rest_coins):
        for i in rest_coins:
            for j in self.machine_coins:
                if i == j.get_nominal():
                    j.decrement_amount()

    def is_enough_money(self):
        return self.user_balance >= self.ticket_cost

    def can_give_rest(self, rest):
        result = False
        temp_machine_coins = self.machine_coins.copy()
        sum_in_machine = 0
        for j in self.user_coins_inside:
            for k in temp_machine_coins:
                if j == k.get_nominal():
                    k.increment_amount()

        for i in temp_machine_coins:
            sum_in_machine += i.value()
        if rest <= sum_in_machine:

            for i in temp_machine_coins:
                logic = True
                while logic:
                    rest = round(rest, 2)
                    if (rest - i.get_nominal() >= 0) \
                            and (i.get_amount() > 0):
                        self.rest_coins.append(i.get_nominal())
                        rest -= i.get_nominal()
                        i.decrement_amount()
                    else:
                        logic = False
            if rest == 0.0:
                result = True
            else:
                self.rest_coins = []
                result = False
        return result

    def clear_users_data(self):
        self.user_coins_inside.clear()
        self.user_balance = 0.0
        self.ticket_cost = 0.0

    def get_ticket_cost(self):
        return round(self.ticket_cost, 2)
