"""
Написать функцию проверяющую валидность введенной даты.

Пример:
    29.02.2000 -> True
    29.02.2001 -> False
    31.04.1962 -> False
"""

import datetime
import re


def validate_date(date: str) -> bool:
    """Вернёт True, если указанная дата валидна, иначе False."""
    try:
        datetime.datetime.strptime(date, '%d.%m.%Y')
        result = True

    except ValueError:
        result = False

    return result


def is_input_format_correct(date: str) -> bool:
    """Вернёт True, если пользователь ввел дату в соответствии с указанным шаблоном, иначе False."""
    return bool(re.search(r'\d{2}[.]\d{2}[.]\d{4}', date))


if __name__ == '__main__':
    while not is_input_format_correct(input_value := input('Введите дату в формате ДД.ММ.ГГГГ ')):
        print('Дата введена некорректно')

    print(input_value, '->', validate_date(input_value))
