def is_prime(number):
    for i in range(2,number//2+1):
        if number%i==0:
            return False
    return True

number = int(input("Введите число: "))
print(is_prime(number))