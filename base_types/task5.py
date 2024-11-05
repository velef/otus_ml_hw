"""
Пользователь вводит данные.
Проверить - являются ли они положительным вещественным числом.
Не использовать встроенные функции для проверки,
только методы данных и конструкцию IF.

Допзадание по желанию - проверка на отрицательные вещественные числа.

Пример:
    5.6 -> True
    .78 -> True
    .67. -> False
    5 -> True
"""

print('Проверка на положительное вещественное число, введите что-нибудь')
number = input()

has_literals = any(char.isalpha() for char in number)
is_negative = number.startswith('-')
is_invalid = number.count('.') > 1

print(number, '->', not (is_negative or has_literals or is_invalid))
