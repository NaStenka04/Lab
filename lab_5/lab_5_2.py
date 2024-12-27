class Circle:

    def __init__ (self, radius):
        self.radius=radius

    def get_radius(self):
        return self.radius
    
    def set_radius(self, new_radius):
        self.radius=new_radius

    
circle1=Circle(5)
print(circle1.get_radius())
f = int(input("Введите новый радиус:"))
circle1.set_radius(f)
print(circle1.radius)

