#__init__ -> Конструктор класса

class Car:
    def __init__(self, model, year):
        self.model = model
        self.year = year


    def info(self):
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")

    @staticmethod
    def get_class_details():
        print("Это класс Car")


    @classmethod
    def get_class_attr(cls):
        cls.count = 1

car = Car(model="Lexus", year=2020)

car.info()



car_1 = Car("BMW", 2022)
car_1.info()
