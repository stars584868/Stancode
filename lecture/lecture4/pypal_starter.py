import pypal


def bank():
    ian_a = pypal.Pypal('Ian', money=1000, withdraw_limit=700)
    ian_a.withdraw(1000)
    ian_a.withdraw(700)
    ian_a.withdraw(700)
    ian_a.n = 'nikita'
    print(ian_a.n)
    ian_a.set_username('niki')
    remaining = ian_a.get_money()
    print(remaining)


if __name__ == '__main__':
    bank()
