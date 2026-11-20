class Parent:
    def earn_money(self):
        print("Родители зарабатывают")

class Father:
    def earn_money(self):
        print("Папа зарабатывает")

class Mother:
    def earn_money(self):
        print("Мама зарабатывает")


class Child(Father, Mother, Parent,):
    # def earn_money(self):
    #     print("Ребенок зарабатывает")
    def play(self):
        print("Ребенок играет")

print(Child.mro())


obj = Child()
obj.play()
obj.earn_money()