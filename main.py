class Vehicle:
    def vehicle_method(self):
        print("Это родительский метод из класса Vehicle")

class Car(Vehicle):
    def car_method(self):
        print("Это метод из дочерного класса Car")

class Cycle(Vehicle):
    def cucle_method(self):
        print("Это метод из дочерного класса Cycle")


obj_v = Vehicle()
obj_v.vehicle_method()

obj_c = Car()
obj_c.car_method()
obj_c.vehicle_method()

obj_cc = Cycle()
obj_cc.cucle_method()
obj_cc.vehicle_method()
