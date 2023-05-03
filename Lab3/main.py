from person import Person
from Employee import Employee
from office import Office

employees = []
employees.append(Employee("nada",10000,10,200))
employees.append(Employee("hamed",10000,10,200))


of1=Office("iti",employees)
print(of1.get_All_employees())



