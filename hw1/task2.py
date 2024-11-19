"""
Пользователь вводит сколько дней осталось до ближайшего отпуска.
Программа должна вывести количество выходных дней до отпуска,
если учесть, что выходные это суббота и воскресенье, сегодня понедельник
и праздники мы не учитываем.

Пример:
    4 -> 0
    6 -> 1
    14 -> 4
"""

print('Сколько дней до отпуска?')
days_before_vacation = int(input())


weeks, days = divmod(days_before_vacation, 7)
weekend_before_vacation = weeks * 2

if days == 6:
    weekend_before_vacation += 1

print(days_before_vacation, '->', weekend_before_vacation)
