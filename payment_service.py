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
        self.change_coins = []

    def init_coins(self):
        for x in range(12):
            self.machine_coins.append(Coin(nominal=Constants.NOMINAL[x], amount=Constants.AMOUNT[x]))

    def add_coin(self, coin):
        self.user_balance += coin
        self.user_coins_inside.append(coin)

    def is_coin_inside(self):
        return self.user_balance > 0.0

    def get_back_coins(self):
        self.change_coins = self.user_coins_inside.copy()

        self.user_balance = 0.0
        self.user_coins_inside.clear()

    def purchase_tickets(self):
        result = False
        if self.user_balance > self.ticket_cost:
            change = self.get_change()
            if self.can_give_change(change):
                self.add_user_coins_to_machine()
                self.withdraw_coins_from_machine(self.change_coins)
                result = True

        elif self.user_balance == self.ticket_cost:
            self.add_user_coins_to_machine()
            result = True
        return result

    def get_change(self):
        return round(self.user_balance - self.ticket_cost, 2)

    def add_user_coins_to_machine(self):
        for i in self.user_coins_inside:
            for j in self.machine_coins:
                if i == j.get_nominal():
                    j.increment_amount()
        self.clear_users_data()

    def withdraw_coins_from_machine(self, change_coins):
        for i in change_coins:
            for j in self.machine_coins:
                if i == j.get_nominal():
                    j.decrement_amount()

    def is_enough_money(self):
        return self.user_balance >= self.ticket_cost

    def can_give_change(self, change):
        result = False
        temp_machine_coins = self.machine_coins.copy()
        sum_in_machine = 0
        for j in self.user_coins_inside:
            for k in temp_machine_coins:
                if j == k.get_nominal():
                    k.increment_amount()

        for i in temp_machine_coins:
            sum_in_machine += i.value()
        if change <= sum_in_machine:

            for i in temp_machine_coins:
                logic = True
                while logic:
                    change = round(change, 2)
                    if (change - i.get_nominal() >= 0) \
                            and (i.get_amount() > 0):
                        self.change_coins.append(i.get_nominal())
                        change -= i.get_nominal()
                        i.decrement_amount()
                    else:
                        logic = False
            if change == 0.0:
                result = True
            else:
                self.change_coins = []
                result = False
        return result

    def clear_users_data(self):
        self.user_coins_inside.clear()
        self.user_balance = 0.0
        self.ticket_cost = 0.0

    def get_ticket_cost(self):
        return round(self.ticket_cost, 2)
