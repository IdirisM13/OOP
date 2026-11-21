class BankAccount:
    def __init__(self, owner: str, balance:int = 0):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Пополнено: {amount}")
        else:
            print(f"Сумма должна быть положительной")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Снято: {amount}")
        else:
            print("Недостаточно средств или некоррекное сумма")
    def get_balance(self):
        return self.__balance



arsen = BankAccount("arsen", 1000)

print(arsen.get_balance())
arsen.deposit(500)
print(arsen.get_balance())


arsen.withdraw(800)
print(arsen.get_balance())

arsen.withdraw(1000)
print(arsen.get_balance())
arsen.deposit(-1000)
print(arsen.get_balance())