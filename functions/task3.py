"""
Функция проверки на простое число.
Простые числа – это такие числа, которые делятся на себя и на единицу.

Пример:
    17 -> True
    20 -> False
    23 -> True
"""


def is_simple(number: int) -> bool:
    """Вернёт True, если число простое, иначе False."""
    if number < 2:
        result = False

    else:
        result = True

        for i in range(2, number):
            if number % i == 0:
                result = False
                break

    return result


def is_digit(row: str) -> bool:
    """Вернёт True, если строка целиком состоит из чисел, иначе False"""
    return all(char.isdigit() for char in row) if row else False
