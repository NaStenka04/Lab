def describe_person(name, age=30):
    print(f"Имя: {name}")
    print(f"Возраст: {age}")

name = input("Введите имя: ")
age = input("Введите возраст: ")
describe_person(name)
describe_person(name, age)