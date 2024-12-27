def read_file(arg):
    with open('lab_3/example.txt', 'r', encoding='utf8') as file:
        if arg=='r':
            content = file.read()
            print(content)
        else:
            for line in file:
                print(line)


arg = input("Введите букву 'r' для чтения файла целиком, "
            "и любую другую для чтения файла построчно: ")
read_file(arg)