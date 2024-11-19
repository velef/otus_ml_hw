"""
Пользователь вводит целое положительное число,
программа должна вернуть строку в виде римского числа.

Пример:
    3 -> III
    15 -> XV
    234 -> CCXXXIV
"""

arab = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
roman = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']

result = ''
i = len(arab) - 1

print('Введите целое положительное число:')
initial_number = int(input())
number = initial_number

while number > 0:
    if number >= arab[i]:
        result += roman[i]
        number -= arab[i]

    else:
        i -= 1

print(f'{initial_number} -> {result}')
