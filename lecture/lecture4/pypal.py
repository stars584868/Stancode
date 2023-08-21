
WITHDRAW_LIMIT = 1000
MONEY = 0


class Pypal:
    def __init__(self, name, money=MONEY, withdraw_limit=WITHDRAW_LIMIT):
        self._n = name
        self.__m = money
        self.wl = withdraw_limit

    def withdraw(self, amount):
        if amount > self.__m:
            print('error')
        elif amount > self.wl:
            print('exceed limit')
        else:
            self.__m -= amount
            print(f'{self._n} remains: {self.__m}')

    def set_username(self, new_name):
        self._n = new_name
        print(f'Successfully updated! New name: {new_name}')

    def get_money(self):
        return self.__m

    def __str__(self):
        return f"{self.n} remains {self.__m}"

    def __iter__(self):
        self.amount = 0
        return self

    def __next__(self):
        self.amount += 100
        if self.amount < self.__m:
            return 100
        else:
            raise StopIteration


def bank():
    ian_a = Pypal('Ian', money=1000, withdraw_limit=700)
    ian_a.withdraw(1000)
    ian_a.withdraw(700)
    ian_a.withdraw(700)


if __name__ == '__main__':
    bank()
