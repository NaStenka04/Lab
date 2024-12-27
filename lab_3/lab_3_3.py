def read_file(arg):
    try:
        file = open("lab_3/example.txt", 'r', encoding='utf8')
    except FileNotFoundError:
        print("Файл не найден")
    else:
        if arg=='r':
            content = file.read()
            print(content)
        else:
            for line in file:
                print(line)
        file.close()


arg = input("Введите букву 'r' для чтения файла целиком, "
            "и любую другую для чтения файла построчно: ")
read_file(arg)