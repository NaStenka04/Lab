class Vehicle:

    def __init__(self, make, model):
        self.make=make
        self.model=model

    def get_info(self):
        return (f'Марка: {self.make}, Модель: {self.model}')
    
class Car (Vehicle):
    
    def __init__(self, make, model, fuel_type):
        super ().__init__(make, model)
        self.fuel_type=fuel_type

    def get_info(self):
        return (f'Марка: {self.make}, Модель: {self.model}, Вид топлива: {self.fuel_type}')
    
v1=Vehicle('Боинг', 'Грузовой 3000Х5') 
c1=Car('Пежо', 'Пикап', 'бензин')   
print(v1.get_info())
print(c1.get_info())