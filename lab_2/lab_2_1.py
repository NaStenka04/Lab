# def greet(name):
#     print(f"Доброе утро, {name}")

# name = input("Введите имя: ")
# greet(name)




# def square(namber):
#     return namber**2

# namber = int(input("Введите число: "))
# print(f"Квадрат числа {namber} равен: {square(namber)}")




def max_of_two(x, y):
    return max(x,y)

num1 = int(input("Введите певое число: "))
num2 = int(input("Введите второе число: "))
if num1==num2:
    print("Числа равны")
else:
    print(f"Большее число: {max_of_two(num1,num2)}")