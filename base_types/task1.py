"""
Пользователь вводит пятизначное число.
Программа должна зеркально отразить центральные три цифры.
Первая и последняя остаются на местах.

Пример:
    23456 -> 25436
    30789 -> 38709
"""

print('Введите пятизначное число:')
number = input()

if len(number) != 5:
    print('Число должно быть пятизначиным')

else:
    print(number, '->', number[0] + number[-2:0:-1] + number[-1])
