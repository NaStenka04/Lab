class Employee:

    def __init__(self, name, id):
        self.name=name
        self.id=id

    def get_info(self):
        return (f'Имя: {self.name}, Идентификационный номер: {self.id}')

class Manager (Employee):

    def __init__(self, name, id, departament):
 #       super ().__init__(name, id)
        Employee.__init__(self, name, id)
        self.departament=departament

    def manage_project(self):
        pass

    def get_info(self):
        return (f'Имя: {self.name}, Идентификационный номер: {self.id}, Отдел: {self.departament}')
    
class Technician (Employee):

    def __init__(self, name, id, specialization):
        super ().__init__(name, id)
        self.specialization=specialization

    def get_info(self):
        return (f'Имя: {self.name}, Идентификационный номер: {self.id}, Специализация: {self.specialization}')

    def perform_maintenance(self):
        pass

class TechManager (Manager, Technician):

    def __init__(self, name, id, departament, specialization, subordinates=None):
        if subordinates is None:
            subordinates = []
        Manager.__init__(self, name, id, departament)
        Technician.__init__(self, name, id, specialization)
        self.subordinates=subordinates

    def add_employee(self, employee):
        self.subordinates.append(employee)

    def get_team_info(self):
        return [emp.get_info() for emp in self.subordinates]
    
    def get_info(self):
        return (f'Имя: {self.name}, Идентификационный номер: {self.id}, Отдел: {self.departament}, Специализация: {self.specialization}')

emp1=Employee('Иван', '111')
emp2=Manager('Кирилл', '222', 'Продаж')
emp3=Technician('Марина', '333', 'Сисадмин')
emp4=TechManager(name='Юлия', id='444', departament='Продаж', specialization='ИТ')
emp4.add_employee(emp1)
emp4.add_employee(emp2)
print(emp1.get_info())
print(emp2.get_info())
print(emp3.get_info())
print(emp4.get_info())
print(emp4.get_team_info())
