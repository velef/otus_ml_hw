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

has_no_literals = all(char.isdecimal() for char in number if char != '.')
is_negative = number.startswith('-')
is_invalid = number.count('.') > 1

print(number, '->', has_no_literals and not (is_negative or is_invalid))
