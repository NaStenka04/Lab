class Book:

    def __init__ (self, title, autor, year):
        self.title=title
        self.autor=autor
        self.year=year

    def get_info(self):
        return (f'Название книги: {self.title}, Автор: {self.autor}, Год издания: {self.year}')
    
book1=Book('Вий','Гоголь Н.В.','1998')
print(book1.get_info())