# 1. Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных будет свидетельствовать пустая строка.
with open("file_1.txt", "w") as file:
    while True:
        a = input("Введите данные для записи в файл: ")
        file.write(a + "\n")
        if not a:
            break
# with open("file_1.txt", "r") as file:
#     content = file.read()
#     print(content)
