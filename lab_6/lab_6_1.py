class UserAccount:


    def __init__(self, username, email, password):
        self.username=username
        self.email=email
        self.__password=password

    def set_password(self, new_password):
        self.__password=new_password

    def check_password(self, password):
        if password==self.__password:
            return True
        return False

        
user1=UserAccount("Ivan", "ivan@bk.ru", "12345678")
new_password=(input("Введите новый пароль: "))
user1.set_password(new_password)
print (user1.check_password(new_password))
print (user1.check_password(12345678))
# print (user1.password)