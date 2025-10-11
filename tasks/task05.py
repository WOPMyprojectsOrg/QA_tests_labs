# Задача: Напишите функцию, которая проверяет, является ли строка палиндромом (игнорируя регистр и пробелы).
# Пример: "A man a plan a canal Panama" → True

def polynom(strk=None):
    if strk is None:
        strk = ""
    strk = str(strk).lower().replace(' ', '')
    print(strk)
    return strk == strk[::-1]

print(polynom())

