from interface import Employee

class FullTimeEmployee(Employee):
    def __init__(self, name, monthly_salary):
        super().__init__(name)
        self.__monthly_salary = monthly_salary # private


    def calculate_salary(self):
        return self.__monthly_salary

class PartTimeEmployee(Employee):
    def __init__(self, name, hours_worked, hourly_rate):
        super().__init__(name)
        self._hours_worked = hours_worked #protect
        self._hourly_rate = hourly_rate #protect

    def calculate_salary(self):
        return self._hours_worked * self._hourly_rate

