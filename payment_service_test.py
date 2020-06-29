import unittest

from Coins import Coin
from payment_service import PaymentService


class TestPaymentService(unittest.TestCase):

    def setUp(self):
        self.payment_service = PaymentService()

    def test_add_coin(self):
        self.assertEqual(self.payment_service.user_balance, 0)
        self.assertFalse(self.payment_service.user_coins_inside)
        self.payment_service.add_coin(0.05)
        self.assertEqual(self.payment_service.user_balance, 0.05)
        self.assertTrue(self.payment_service.user_coins_inside)

    def test_clear_user_data(self):
        self.assertEqual(self.payment_service.user_balance, 0.0)
        self.payment_service.add_coin(0.05)
        self.assertEqual(self.payment_service.user_balance, 0.05)
        self.assertTrue(self.payment_service.user_coins_inside)
        self.payment_service.clear_users_data()
        self.assertEqual(self.payment_service.user_balance, 0.00)
        self.assertFalse(self.payment_service.user_coins_inside)

    def test_is_coin_inside(self):
        self.payment_service.add_coin(0.05)
        self.assertTrue(self.payment_service.is_coin_inside())

    def test_get_back_coins(self):
        self.payment_service.add_coin(1.0)
        self.assertEqual(self.payment_service.user_balance, 1.0)
        self.assertFalse(self.payment_service.rest_coins)
        self.assertTrue(self.payment_service.user_coins_inside)

        self.payment_service.get_back_coins()

        self.assertEqual(self.payment_service.user_balance, 0.0)
        self.assertTrue(self.payment_service.rest_coins)
        self.assertFalse(self.payment_service.user_coins_inside)

    def test_purchase_tickets_not_enough_many(self):
        self.payment_service.ticket_cost = 5.0
        self.payment_service.add_coin(2.0)
        self.assertFalse(self.payment_service.purchase_tickets())

    def test_purchase_tickets_without_rest(self):
        self.payment_service.ticket_cost = 5.0
        self.payment_service.add_coin(5.0)
        self.assertTrue(self.payment_service.purchase_tickets())

    def test_purchase_tickets_with_rest(self):
        self.payment_service.ticket_cost = 5.0
        self.payment_service.add_coin(10.0)
        self.assertTrue(self.payment_service.purchase_tickets())

    def test_can_give_rest(self):
        coins_in_machine = [Coin(nominal=0.1, amount=1),
                            Coin(nominal=0.1, amount=1),
                            Coin(nominal=0.2, amount=1)]
        self.payment_service.machine_coins = coins_in_machine
        self.payment_service.ticket_cost = 4.60
        self.payment_service.add_coin(5.0)
        self.assertTrue(self.payment_service.can_give_rest(self.payment_service.get_rest()))

    def test_can_not_give_rest(self):
        self.payment_service.machine_coins = [Coin(nominal=0.5, amount=1)]
        self.payment_service.ticket_cost = 4.60
        self.payment_service.add_coin(5.0)
        self.assertFalse(self.payment_service.can_give_rest(self.payment_service.get_rest()))

    def test_can_not_give_rest_not_money(self):
        self.payment_service.machine_coins = [Coin(nominal=0.5, amount=1)]
        self.payment_service.ticket_cost = 4.40
        self.payment_service.add_coin(5.0)
        self.assertFalse(self.payment_service.can_give_rest(self.payment_service.get_rest()))

    def test_add_user_coins_to_machine(self):
        self.payment_service.machine_coins = [Coin(nominal=0.5, amount=1),
                                              Coin(nominal=0.2, amount=0),
                                              Coin(nominal=0.1, amount=0)]
        self.payment_service.user_coins_inside = [0.5, 0.5, 0.2, 0.1]
        self.payment_service.add_user_coins_to_machine()
        self.assertFalse(self.payment_service.user_coins_inside)
        expected_sum_in_machine = 1.80
        actual_sum_in_machine = 0.0
        for coin in self.payment_service.machine_coins:
            actual_sum_in_machine += coin.value()

        self.assertEqual(actual_sum_in_machine, expected_sum_in_machine)

    def test_withdraw_coins_from_machine(self):
        self.payment_service.machine_coins = [Coin(nominal=0.5, amount=1),
                                              Coin(nominal=0.2, amount=2),
                                              Coin(nominal=0.1, amount=2)]
        self.payment_service.rest_coins = [0.5, 0.2, 0.1]
        self.payment_service.withdraw_coins_from_machine(self.payment_service.rest_coins)
        expected_sum_in_machine = 0.3
        actual_sum_in_machine = 0.0
        for coin in self.payment_service.machine_coins:
            actual_sum_in_machine += coin.value()

        self.assertEqual(round(actual_sum_in_machine, 2), expected_sum_in_machine)


if __name__ == '__main__':
    unittest.main()
