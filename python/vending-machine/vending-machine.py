from typing import Tuple
class VendingMachine:
    def __init__(self):
        self.coin_inventory = {
            0.25: 100,
            0.10: 100,
            0.05: 100,
            0.01: 100
        }
        self.inserted_cash = 0.0
        self.item_price = 0.0
        self.change_due = 0.0

    def accept_coins(self, coin_value: float) -> Tuple[bool, str]:
        if coin_value not in self.coin_inventory.keys():
            return False, 'Invalid coin'
        self.inserted_cash += coin_value
        self.coin_inventory[coin_value] += 1
        return True, f'Accepted {coin_value}. Total inserted = {self.inserted_cash}'

    def calculate_change(self, item_price) -> Tuple[bool, str]:
        if self.inserted_cash < item_price:
            return False, f'Insufficient funds. Please insert {self.item_price - self.inserted_cash} more'

        self.change_due = round(self.inserted_cash - item_price, 2)
        return True, f'Change due: {self.change_due}'

    def dispense_change(self) -> Tuple[bool, str]:
        # dispense using greedy, largest coins first
        coins_to_dispense = []
        remaining_change = self.change_due

        for coin in sorted(self.coin_inventory.keys(), reverse=True):
            if coin > remaining_change:
                continue
            if remaining_change <= 0:
                break
            num_of_coins = min(int(remaining_change / coin), self.coin_inventory[coin])

            coins_to_dispense.extend([coin] * num_of_coins)
            remaining_change = round(remaining_change - (num_of_coins * coin), 2)
        if remaining_change > 0:
            # not enough change available, so just cancel
            for coin in coins_to_dispense:
                self.coin_inventory[coin] += 1
            return False, 'Insufficient Change'
        return True, f'Dispensing {coins_to_dispense}'



if __name__ == '__main__':
    vm = VendingMachine()
    print(vm.accept_coins(0.25))
    print(vm.accept_coins(0.25))
    print(vm.accept_coins(0.25))
    print(vm.accept_coins(0.25))

    # buy an item
    print(vm.calculate_change(0.69))

    # dispense change
    print(vm.dispense_change())
