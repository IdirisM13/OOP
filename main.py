from service import FullTimeEmployee, PartTimeEmployee

from interface import Employee

def print_salary(employee: Employee):
    print(f"{employee.name}: {employee.calculate_salary()} som")

fti = FullTimeEmployee("Aybek", 80000)
pte = PartTimeEmployee("Alina", 80, 500)
print_salary(fti)
print_salary(pte)



