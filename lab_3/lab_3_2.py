def write_in_file(text):
    with open('lab_3/user_input.txt', 'a', encoding='utf8') as file:
        file.write(text)

text = input("Введите текст: ")
write_in_file(text)