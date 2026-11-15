# Класс это структура данных, котороя служит для описание объектов
class Person:
    name: str = "Asan"  # Свойства -> Атрибуты
    age: int = 23  # Свойства -> Атрибуты

    def sleep(self):  # Поведение -> Метод
        print(f"{self.name} Спит")

    def run(self):
        print(f"{self.name} running")


person_1 = Person()  # first object
print(person_1.name)
print(person_1.age)
person_1.sleep()
person_1.run()

person_2 = Person()
person_2.name = "Uson"
person_2.age = 24
print(person_2.name)
print(person_2.age)
person_2.sleep()
person_2.run()
